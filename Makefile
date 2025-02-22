SHELL = /bin/bash
APP_DIR = py_apps


default: install

all: hooks exp install fmt-check lint ti typecheck


h help:
	@grep '^[a-z]' Makefile


.PHONY: hooks
hooks:
	cd .git/hooks && ln -s -f ../../hooks/pre-push pre-push


install:
	pip install pip --upgrade
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

upgrade:
	pip install pip --upgrade
	pip install -r requirements.txt --upgrade
	pip install -r requirements-dev.txt --upgrade


fmt:
	black .
	isort .

fmt-check:
	black . --diff --check
	isort . --diff --check-only

pylint:
	pylint $(APP_DIR) \
		|| pylint-exit $$?

flake8:
	# Error on syntax errors or undefined names.
	flake8 . --select=E9,F63,F7,F82 --show-source
	# Warn on everything else.
	flake8 . --exit-zero

lint: pylint flake8

fix: fmt lint

# Delete the above and use this instead if Ruff is preferred.
fmt-r:
	ruff check

fix-r:
	ruff check --fix


t typecheck:
	mypy $(APP_DIR) tests

ti typeinstall:
	yes | mypy --install-types

test:
	pytest

run:
	python3 -m ${APP_DIR}.main

exp:
	# Export dependencies for pip
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	# Export dev dependencies for pip
	poetry export -f requirements.txt --only dev --output requirements-dev.txt --without-hashes

clean:
	@# Remove old built files
	rm -rfv build/ dist/

pack:
	tar -czvf dist/${APP_DIR}.tar.gz dist/${APP_DIR}

build: clean
	pyinstaller main.spec
	mv dist/main dist/${APP_DIR}
	mv dist/${APP_DIR}/main dist/${APP_DIR}/py-apps
