SHELL := /bin/bash

DIR := $(dir $(lastword $(MAKEFILE_LIST)))
APP_NAME := tdd

buildup:
	docker compose up --build

buildupd:
	docker compose up -d --build

build_dev:
	-docker exec $(APP_NAME)-app /bin/sh -c 'pip install black ruff'

fmt:
	-docker exec $(APP_NAME)-app /bin/sh -c 'black .'

lint:
	-docker exec $(APP_NAME)-app /bin/sh -c 'ruff .'

lintf:
	-docker exec $(APP_NAME)-app /bin/sh -c 'ruff --fix .'

up:
	docker compose up

upd:
	docker compose up -d

start:
	docker compose start

stop:
	docker compose stop

restart:
	docker compose restart

rm:
	-docker stop $$(docker ps -aqf "name=${APP_NAME}")
	-docker rm $$(docker ps -aqf "name=${APP_NAME}")

rmi: rm
	-docker rmi $$(docker images | grep '${APP_NAME}' | awk '{print$$3}')
	-docker network rm $$(docker network ls | grep $(APP_NAME) | awk '{print$$2}')

logsf:
	docker compose logs -f

logs:
	docker compose logs
