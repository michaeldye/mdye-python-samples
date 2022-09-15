# Python and virtual environment setup

## Quick option: System-provided Python and a manual venv

* Use your system's package manager to install a suitable Python version, like 3.9.14. If you're using a Debian-based distribution, try `sudo apt install python3.9`; if using a RedHat-based distribution, try `sudo dnf install python39`. If using MacOS with homebrew, try `sudo brew install python@3.9`

  * Check your python version by executing:

    ```
    python --version

    Python 3.9.14
    ```
* In the root of this project's directory, create a venv:

  ```
  python -m venv ./venv
  ```

Now activate the virtualenv and note that your `PYTHON_PATH` has been modified and your shell prompt has the prefix `(venv)`. 

```
source ./venv/bin/activate

(venv) mdye-python-samples[1]# echo $VIRTUAL_ENV
/home/mdye/projects/mdye-python-samples/venv
```

To exit the venv, execute `deactivate`.


## Managed option: direnv and pyenv

This project can use a direnv-managed Python venv with pyenv-managed Python version. If you want to use this
option, perform the following steps:

* Install [pyenv](https://github.com/pyenv/pyenv)
* After completing the pyenv installation steps through [Install Python build dependencies](https://github.com/pyenv/pyenv#install-python-build-dependencies), install an interpreter like python 3.9.14 (this builds an interpreter from source and so may take a few minutes):

  ```
  pyenv install 3.9.14
  ```

* Install [direnv](https://direnv.net/)
* Copy the provided `.envrc-EXAMPLE` to `.envrc` and set `PYENV_VERSION` to the version string you installed with pyenv earlier
* Enable direnv by executing `direnv allow .envrc`, this will create a virtual environment for you (if necessary) and activate it:

  ```mdye-python-samples[2]# direnv allow .envrc

  direnv: loading ~/projects/mdye-python-samples/.envrc
  direnv: export +PYENV_VERSION +VIRTUAL_ENV ~PATH
  ```

Every time you cd into the project directory, mdye-python-samples, direnv will automatically activate your virtual environment.

### Troubleshooting

* If the command `pyenv` isn't found, plesae ensure your shell is setup correctly
* If you haven't synced the pyenv project in a while, the version you desire might not be available. If this is the case, try executing something like `(cd ~/.pyenv && git pull)` before installing a new pyenv version
