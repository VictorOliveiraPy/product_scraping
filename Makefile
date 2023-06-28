DOCKER_COMPOSE=docker-compose

.DEFAULT_GOAL := build

build:
	@echo "BUILDING THE APP"
	-$(DOCKER_COMPOSE) build $(APP_NAME)

build:
	-$(DOCKER_COMPOSE) up --build mongo -d

run:
	-$(DOCKER_COMPOSE) up app

stop:
	@echo "STOPPING CONTAINERS"
	-$(DOCKER_COMPOSE) stop

down:
	@echo "REMOVING CONTAINERS"
	-$(DOCKER_COMPOSE) down

remove:
	@echo "REMOVING CONTAINERS AND VOLUMES"
	-$(DOCKER_COMPOSE) down -v


setup: build up-db


test:
	-$(DOCKER_COMPOSE) run app python -m pytest --cov="."

.PHONY:test