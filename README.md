# `mdye-python-samples`

[![Unit Test Status](https://github.com/michaeldye/mdye-python-samples/actions/workflows/python-app.yaml/badge.svg)](https://github.com/michaeldye/mdye-python-samples/actions)

A repo of small Python code samples. Some are related to programming puzzle /
practice sites like [LeetCode](https://leetcode.com) (in [src/mdye_leetcode](src/mdye_leetcode)) or [Project
Euler](https://projecteuler.net) in [src/mdye_euler](src/mdye_euler). All code assumes a recent version of Python,
like 3.9.0 or newer. (See `pyproject.toml` for precise dependency declaration).


## One-time Setup

### Step 1: Set up a Python interpreter and virtual environment

If you don't already have a suitable Python interpreter and virtual environment, consult [doc/environment_setup.md](doc/environment_setup.md)

### Step 2: Install Poetry

Once you've set up an environment, ensure you are in an active Python virtual environment by doing something like this:

    echo $VIRTUAL_ENV && which python && which pip
    
    /home/mdye/projects/mdye-python-samples/.direnv/python-3.9.14
    ~/projects/mdye-python-samples/.direnv/python-3.9.14/bin/python
    ~/projects/mdye-python-samples/.direnv/python-3.9.14/bin/pip

Now install [poetry](https://pypi.org/project/poetry/):

    pip install poetry
    
    ...
    Successfully installed ... poetry-1.2.0 poetry-core-1.1.0 ... 
    ...

### Step 3: Install this project's code in your virtual environment

Finally, install this project's code (in packages described in pyproject.toml) in your virtual env:

    poetry install
    
    ...
    Installing the current project: mdye-python-samples (0.1.0)


## Project Use

### Execute solutions

All mature code puzzle solutions are tested by pytest. To execute tests in this project, execute:

    pytest

    ==================================================== test session starts ====================================================
    platform linux -- Python 3.9.13, pytest-7.1.3, pluggy-1.0.0
    rootdir: /home/mdye/projects/mdye-python-samples, configfile: pyproject.toml
    collected 12 items                                                                                                          
    
    src/mdye_euler/test/test_solution_1.py::test_solution PASSED                                                          [  8%]
    src/mdye_euler/test/test_solution_2.py::test_solution PASSED                                                          [ 16%]
    src/mdye_euler/test/test_solution_3.py::test_lpf_small PASSED                                                         [ 25%]
    
    ...
    ==================================================== 12 passed in 0.14s =====================================================


To execute tests for only a specific puzzle site, for example `leetcode` provide pytest with the project directory in which to search for tests:

    pytest ./src/mdye_leetcode
    ==================================================== test session starts ====================================================
    platform linux -- Python 3.9.13, pytest-7.1.3, pluggy-1.0.0
    rootdir: /home/mdye/projects/mdye-python-samples, configfile: pyproject.toml
    collected 8 items                                                                                                           
    
    src/mdye_leetcode/test/test_solution_1060.py::test_solution_5_basic PASSED                                            [ 12%]
    src/mdye_leetcode/test/test_solution_1491.py::test_solution_1491_basic PASSED                                         [ 25%]

    ...
    ===================================================== 8 passed in 0.04s =====================================================
    
### Execute miscellaneous code samples

For content in `mdye_misc`, execute modules directly with the necessary cli args. For example:

    ./src/mdye_misc/fib_various.py 20

    Note: not making an effort to warm the thread so timing values may vary widely
    {'fn_name': 'calc_fib_dp', 'time_s': '1.16825e-05'}
    {'fn_name': 'calc_fib_memo', 'time_s': '6.65188e-05'}
    {'fn_name': 'calc_fib_naive', 'time_s': '0.00445795'}
    20th fib: 6765

.. or:

    ./src/mdye_misc/heaps.py 

    priority order after popping top of heap each time:
    [65, 42, 32, 22, 19, 19, 12, 7, 7, 6, 6, 5, 2, 1, 1]
    done
