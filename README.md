# python_uarch_bench

**Microarchitectural Benchmarking Framework for Python**

`python_uarch_bench` is a framework aimed at benchmarking and analyzing microarchitectural performance characteristics of Python code. It facilitates the exploration of how Python programs interact with underlying hardware components such as the CPU pipeline, cache hierarchy, and branch predictors.
---

## Features

- **Microarchitectural Analysis**: Assess the impact of Python code on CPU microarchitecture, including instruction pipelines and cache usage.
- **Benchmarking Suite**: Run a series of benchmarks to evaluate performance metrics under different scenarios.
- **Extensibility**: Easily add new benchmarks or analysis tools to tailor the framework to specific needs.
---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- [pip](https://pip.pypa.io/en/stable/)
- Optional: [Nix](https://nixos.org/) for environment management

### Installation
    ```
    pip install python_uarch_bench
    ```

### Running Benchmarks
To execute the benchmark suite:

```
python -m python_uarch_bench
```
