# Makefile is just a wrapper around tox commands
SHELL := /bin/bash

USER_ID := $(shell id -u)
GROUP_ID := $(shell id -g)
APP_NAME := adsp
APP_VERSION := $(shell git describe --tags --dirty --always)
CURRENT_UNIX_EPOCH_TIMESTAMP := $(shell date +%s)

FORCE_ID := avon-and-somerset
MONTH := 2023-04
CSV_FILE := output.csv


.PHONY: all
all: build

.PHONY: build-image
build-image:
	@echo "[Building image with build time]"
	docker build \
	--build-arg APP_VERSION=$(APP_VERSION) \
	--build-arg BUILD_TIME=$(CURRENT_UNIX_EPOCH_TIMESTAMP) \
	--tag $(APP_NAME):$(APP_VERSION) .

.PHONY: run-image
run-image:
	@echo "[Run docker image]"
	docker run -it -d \
	--name $(APP_NAME) \
	$(APP_NAME):$(APP_VERSION) \
	bash

.PHONY: build
build:
	tox -e build-dists

.PHONY: test
test:
	tox

.PHONY: check
check:
	tox -e checkqa
