#!/usr/bin/env python3
""" test the wrapper """

from python_uarch_bench.uarch_bench import parse_uarch_bench_output, get_uarch_bench_data


def test_simple():
    """ if this test fails, something is really of """
    file = "./test/data/zen4.txt"
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        metadata, groups = parse_uarch_bench_output(lines)
        print(metadata)
        print(groups)


def test_get_data():
    """ test `get_uarch_bench_data()` """
    b, metadata, groups = get_uarch_bench_data()
    assert b


if __name__ == "__main__":
    test_simple()
