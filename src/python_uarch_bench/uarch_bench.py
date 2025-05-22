#!/usr/bin/env python3
import re
from collections import defaultdict
from typing import Union, Tuple, List
import pprint
from subprocess import PIPE, STDOUT, Popen


def parse_uarch_bench_output(lines: List[str]) -> Tuple[dict, dict]:
    """
    :param text
    :return 
        metadata = {},
        groups = {
            'basic': [
                {'benchmark': 'Dependent add chain', 'cycles': 1.0, 'nanos': 0.18},
                ...
            ],
            'bmi': ...
        }
    """
    groups = defaultdict(list)
    metadata = {}
    current_group = None
    r = re.compile(r'^\s*(.*?)\s+([\d.]+)\s+([\d.]+)\s*$')
    g = re.compile(r"\*\* Running group (.+?) \*\*")

    for line in lines:
        # Parse metadata (non-benchmark key-value pairs)
        if not current_group and ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            metadata[key] = value

        # Detect group headers
        group_match = g.findall(line)
        if group_match:
            current_group = group_match[0]
            assert ":" in current_group

            pos = current_group.find(":")
            current_group = current_group[:pos].strip()
            continue

        # Detect benchmarks
        bench_match = r.findall(line)
        if bench_match and current_group:
            assert len(bench_match) == 1
            bench_match = bench_match[0]

            assert len(bench_match) == 3
            benchmark, cycles, nanos = bench_match
            groups[current_group].append({
                "benchmark": benchmark.strip(),
                "cycles": float(cycles),
                "nanos": float(nanos)
            })
            continue

    return metadata, dict(groups)
    #return {
    #    "metadata": metadata,
    #    "benchmark_groups": dict(groups)
    #}


def get_uarch_bench_data() -> Tuple[bool, dict, dict]:
    """
    :return the output from the `./uarch_bench.sh` script
    """
    CMD = "deps/uarch-bench/uarch-bench.sh"
    with Popen([CMD, "--verbose"], stdout=PIPE, stderr=STDOUT) as p:
        p.wait()
        if p.returncode != 0:
            print("command failed")
            return False, {}, {}

        assert p.stdout
        s = p.stdout.readlines()
        s = [str(a.decode().removesuffix("\n")) for a in s]
        metadata, groups = parse_uarch_bench_output(s)
        return True, metadata, groups
