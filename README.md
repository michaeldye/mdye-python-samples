# `mdye-python-samples`

[![Status](https://github.com/michaeldye/mdye-python-samples/actions/workflows/python-app.yaml/badge.svg)](https://github.com/michaeldye/mdye-python-samples/actions)

## Introduction

A repo of small Python code samples. Some are related to programming puzzle /
practice sites.

* [LeetCode](https://leetcode.com) solutions can be found in [src/mdye_leetcode](src/mdye_leetcode); unit tests are in [src/mdye_leetcode/test](src/mdye_leetcode/test)
+ [HackerRank](https://www.hackerrank.com) solutions can be found in [src/mdye_hackerrank](src/mdye_hackerrank); unit tests are in [src/mdye_hackerrank/test](src/mdye_hackerrank/test)
* [Project Euler](https://projecteuler.net) solutions can be found in [src/mdye_euler](src/mdye_euler); unit tests are in [src/mdye_euler/test](src/mdye_euler/test)

## Preconditions

All code assumes a recent version of Python, like 3.9.0 or newer. (See `pyproject.toml` for precise dependency declaration). It also requires the [Poetry](https://python-poetry.org/) packaging and dependency management system and GNU make.

## Use

You can execute tests for all puzzles and code samples (followed by code linting) by invoking `make`:

```shell
$ make
++ install-deps
...

Installing the current project: mdye-python-samples (0.1.0)
++ pytest
====================================== test session starts =======================================
platform linux -- Python 3.12.7, pytest-8.3.3, pluggy-1.5.0
rootdir: /home/mdye/projects/mdye-python-samples
configfile: pyproject.toml
collected 51 items

src/mdye_euler/test/test_solution1.py::test_solution PASSED                                [  1%]
src/mdye_euler/test/test_solution_2.py::test_solution PASSED                               [  3%]
...
src/mdye_misc/test/test_sliding_window.py::test_avg_of_subarray_reuse_sum PASSED           [100%]

======================================= 51 passed in 0.26s =======================================
++ lint
All checks passed!
```

## Miscellaneous

### Useful project management invocations

Note that the following expect you've properly set up the project as described below.

* `make test`: Execute all test in the system; note that CI will reject PRs if tests fail
* `make format`: Format all code with `ruff`
* `make lint`: Lint code with `ruff`
* `make fix`: Do safe fixes suggested by `ruff`
* `make inspect` (`all` / default): Do linting and tests
* `make precommit`: Format code, execute tests, and do lint inspection

### Test execution options

#### Specific puzzles
To execute tests for only a specific puzzle site, for example `leetcode` provide pytest with the project directory in which to search for tests:

```shell
$ poetry run pytest ./src/mdye_leetcode

================================================ test session starts ============================
platform linux -- Python 3.9.13, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/mdye/projects/mdye-python-samples, configfile: pyproject.toml
collected 8 items

src/mdye_leetcode/test/test_solution_1060.py::test_solution_5_basic PASSED                 [ 12%]
src/mdye_leetcode/test/test_solution_1491.py::test_solution_1491_basic PASSED              [ 25%]

...
===================================================== 8 passed in 0.04s =========================
```

#### Pytest with stdout / stderr

```shell
$ poetry run pytest -s ./src
...
```

#### Code Samples

To execute miscellaneous code samples (those in `mdye_misc`), execute modules directly with the necessary cli args. For example:

```shell
$ poetry run ./src/mdye_misc/fib_various.py 20

Note: not making an effort to warm the thread so timing values may vary widely
{'fn_name': 'calc_fib_dp', 'time_s': '1.16825e-05'}
{'fn_name': 'calc_fib_memo', 'time_s': '6.65188e-05'}
{'fn_name': 'calc_fib_naive', 'time_s': '0.00445795'}
20th fib: 6765
```
