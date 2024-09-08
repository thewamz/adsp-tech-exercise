# Makefile is just a wrapper around tox commands

.PHONY: build
build:
	tox -e build-dists

.PHONY: test
test:
	tox

.PHONY: check
check:
	tox -e checkqa
