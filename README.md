# `mdye-python-samples`

[![Status](https://github.com/michaeldye/mdye-python-samples/actions/workflows/python-app.yaml/badge.svg)](https://github.com/michaeldye/mdye-python-samples/actions)

## Introduction 

A repo of small Python code samples. Some are related to programming puzzle /
practice sites.

* [LeetCode](https://leetcode.com) solutions can be found in [src/mdye_leetcode](src/mdye_leetcode); unit tests are in [src/mdye_leetcode/test](src/mdye_leetcode/test)
* [Project Euler](https://projecteuler.net) solutions can be found in [src/mdye_euler](src/mdye_euler); unit tests are in [src/mdye_euler/test](src/mdye_euler/test)

Given appropriate setup, you can execute tests for all puzzles and code samples (followed by code linting) by invoking:

```shell
$ make
++ pytest
================================================ test session starts ============================
platform linux -- Python 3.9.13, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/mdye/projects/mdye-python-samples, configfile: pyproject.toml
collected 12 items                                                                                

src/mdye_euler/test/test_solution_1.py::test_solution PASSED                               [  8%]
...
src/mdye_leetcode/test/test_solution_1060.py::test_solution_1060_basic PASSED              [ 41%]
..
src/mdye_leetcode/test/test_solution_823.py::test_solution_823_deep PASSED                 [100%]

================================================= 12 passed in 0.12s ============================
++ pylint

--------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 10.00/10, +0.00)

```

## Useful project management invocations

Note that the following expect you've properly set up the project as described below.

* `make test`: Execute all test in the system; note that CI will reject PRs if tests fail
* `make format`: Format all code with `black`
* `make lint`: Lint code with `pylint`; note that CI will reject PRs if the codebase receives a lower pylint score than the `main` branch last had
* `make inspect` (`all` / default): Do linting and tests
* `make precommit`: Format code, execute tests, and do lint inspection

* `new-solution --kind {leetcode,euler} --number {solution_number}`: Create a new solution (of the appropriate type) with a templated solution implementation module and `pytest` stub


## Project Setup

### Step 1: Set up a Python interpreter and virtual environment

All code assumes a recent version of Python, like 3.9.0 or newer. (See `pyproject.toml` for precise dependency declaration). If you don't already have a suitable Python interpreter and virtual environment, consult [doc/environment_setup.md](doc/environment_setup.md).

### Step 2: Install Poetry

Once you've set up an environment, ensure you are in an active Python virtual environment by doing something like this:

```shell
$ echo $VIRTUAL_ENV && which python && which pip

/home/mdye/projects/mdye-python-samples/.direnv/python-3.9.14
~/projects/mdye-python-samples/.direnv/python-3.9.14/bin/python
~/projects/mdye-python-samples/.direnv/python-3.9.14/bin/pip
```

Install project dependencies (like [poetry](https://pypi.org/project/poetry/)) and this project's package:

```shell
$ make install-deps

...
Successfully installed ... poetry-1.2.0 poetry-core-1.1.0 ... 
...
Installing the current project: mdye-python-samples (0.1.0)
```

## Test execution options

### Specific puzzles
To execute tests for only a specific puzzle site, for example `leetcode` provide pytest with the project directory in which to search for tests:

```shell
$ pytest ./src/mdye_leetcode

================================================ test session starts ============================
platform linux -- Python 3.9.13, pytest-7.1.3, pluggy-1.0.0
rootdir: /home/mdye/projects/mdye-python-samples, configfile: pyproject.toml
collected 8 items                                                                                

src/mdye_leetcode/test/test_solution_1060.py::test_solution_5_basic PASSED                 [ 12%]
src/mdye_leetcode/test/test_solution_1491.py::test_solution_1491_basic PASSED              [ 25%]

...
===================================================== 8 passed in 0.04s =========================
```

### Pytest with stdout

```shell
$ pytest -s ./src
...
```

### Code Samples
    
To execute miscellaneous code samples (those in `mdye_misc`), execute modules directly with the necessary cli args. For example:

```shell
$ ./src/mdye_misc/fib_various.py 20

Note: not making an effort to warm the thread so timing values may vary widely
{'fn_name': 'calc_fib_dp', 'time_s': '1.16825e-05'}
{'fn_name': 'calc_fib_memo', 'time_s': '6.65188e-05'}
{'fn_name': 'calc_fib_naive', 'time_s': '0.00445795'}
20th fib: 6765
```

... or:

```shell
$ ./src/mdye_misc/heaps.py

priority order after popping top of heap each time:
[65, 42, 32, 22, 19, 19, 12, 7, 7, 6, 6, 5, 2, 1, 1]
done
```
