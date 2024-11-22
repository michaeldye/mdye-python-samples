SHELL := /usr/bin/env TZ=UTC bash

SRC := $(CURDIR)/src

ifndef verbose
.SILENT:
endif

all: inspect

distclean:
	@echo "++ $@"
	find . \( -name "__pycache__" -or -path "./build*" -or -path "./.pytest_cache*" -or -path "./dist" \) -exec rm -Rf {} +

pristine: distclean
	@echo "++ $@"
	-git checkout .
	-git reset --hard HEAD
	-git clean -fdx

show-make:
	which make
	make --version

install-deps:
	@echo "++ $@"
	poetry install

check: test

inspect: check lint

precommit: format inspect

test: pytest

pytest: | install-deps
	@echo "++ $@"
	poetry run pytest

lint: $(SRC) | install-deps
	@echo "++ $@"
	poetry run ruff check $^

format: $(SRC) | install-deps
	@echo "++ $@"
	poetry run ruff format $^

fix: $(SRC) | install-deps
	@echo "++ $@"
	poetry run ruff check --fix $^

.PHONY: all check fix format inspect lint test precommit pytest show-make
