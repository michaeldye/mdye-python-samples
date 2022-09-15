# `mdye-python-samples`

[![Unit Test Status](https://github.com/michaeldye/mdye-python-samples/actions/workflows/python-app.yaml/badge.svg)](https://github.com/michaeldye/mdye-python-samples/actions)

A repo of small Python code samples. Some are related to programming puzzle /
practice sites like [LeetCode](https://leetcode.com) or [Project
Euler](https://projecteuler.net). All code assumes a recent version of Python,
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

To execute tests for only a specific puzzle site, for example `leetcode` provide pytest with the project directory in which to search for tests:

    pytest ./src/mdye_leetcode

### Execute miscellaneous code samples

For content in `mdye_misc`, execute modules directly with the necessary cli args. For example:

    ./src/mdye_misc/fib_various.py 100
    
    ...

.. or:

    ./heaps.py
    
    ...
