SHELL := /usr/bin/env TZ=UTC bash

SRC := $(CURDIR)/src


ifeq ($(SKIP_VENV_CHECK),)
	exec-prefix =
else
	exec-prefix = poetry run
endif


# spooky that github actions' make needs this here (after var setup, just before targets)
ifndef verbose
.SILENT:
endif

all: check lint

show-make:
	which make
	make --version

check-in-venv:
	if [[ -z "$${SKIP_VENV_CHECK:-}" ]]; then \
	  if [[ "$$VIRTUAL_ENV" == "" ]] || [[ ! -d "$$VIRTUAL_ENV" ]] ; then \
	    echo "ERROR: Not in Python VENV" >&2 && \
	    exit 55; \
	  fi; \
	fi

install-deps: | check-in-venv
	@echo "++ $@"
	python -m pip install poetry
	poetry install

check: test

test: pytest

pytest: | check-in-venv
	@echo "++ $@"
	#$(conditionally-in-poetry)
	$(exec-prefix) $@

lint: pylint

pylint: $(SRC) | check-in-venv
	@echo "++ $@"
	#$(conditionally-in-poetry)
	$(exec-prefix) $@ $^



.PHONY: all check check-in-venv lint test pylint pytest show-make
