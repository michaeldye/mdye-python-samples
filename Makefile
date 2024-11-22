SHELL := /usr/bin/env TZ=UTC bash

SRC := $(CURDIR)/src


# spooky that github actions' make needs this here (after var setup, just before targets)
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

pytest:
	@echo "++ $@"
	poetry run pytest

lint: $(SRC)
	@echo "++ $@"
	poetry run ruff check $^

format: $(SRC)
	@echo "++ $@"
	poetry run ruff format $^

.PHONY: all check format inspect lint test precommit pytest show-make
