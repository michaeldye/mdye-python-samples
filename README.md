# `mdye-python-samples`

[![Unit Test Status](https://github.com/michaeldye/mdye-python-samples/actions/workflows/python-app.yaml/badge.svg)](https://github.com/michaeldye/mdye-python-samples/actions)

A repo of small Python code samples. Some are related to programming puzzle /
practice sites like [LeetCode](https://leetcode.com) or [Project
Euler](https://projecteuler.net). All code assumes a recent version of python,
like 3.9.0 or newer. (See `pyproject.toml` for precise dependency declaration).

## Project Use

### One-time Setup

#### Set up Environment

Below are steps for two different ways to set up a Python virtual environment if you don't already have one.

##### Quick option: System-provided Python and a manual venv

* Use your system's package manager to install a suitable Python versoin, like 3.9.14. If you're using a Debian-based distribution, try `sudo apt install python3.9`; if using a RedHat-based distribution, try `sudo dnf install python39`. If using MacOS with homebrew, try `sudo brew install python@3.9`

  * Check your python version by executing:

    ```
    python --version
    ```
* In the root of this project's directory, create a venv:

  ```
  python -m venv ./venv
  ```

##### Managed option: direnv and pyenv

This project includes a direnv-managed Python venv. If you want to use this
option, perform the following steps:

* Install [pyenv](https://github.com/pyenv/pyenv)
  * After completing the installation steps through [Install Python build dependencies](https://github.com/pyenv/pyenv#install-python-build-dependencies), install an interpreter like python 3.9.14:

    ```
    pyenv install 3.9.14
    ```

    * If the command `pyenv` isn't found, plesae ensure your shell is setup correctly
    * If you haven't synced the pyenv project in a while, the version you desire might not be available. If this is the case, try executing something like `(cd ~/.pyenv && git pull)` before installing a new pyenv version

* Install [direnv](https://direnv.net/)
  * Copy the provided `.envrc-EXAMPLE` to `.envrc` and set `PYENV_VERSION` to the version string you installed with pyenv earlier
  * Enable direnv by executing `direnv allow .envrc`, this will create a virtual environment for you (if necessary) and activate it


#### Install Poetry

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

#### Install this project's code in your virtual environment

Finally, install this project's code (in packages described in pyproject.toml) in your virtual env:

    poetry install
    
    ...
    Installing the current project: mdye-python-samples (0.1.0)


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
