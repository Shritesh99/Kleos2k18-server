.PHONY: all build push deploy run stop

all: build push deploy

build:
	docker build -t shritesh99/kleos2k18:latest .

push:
	docker push shritesh99/kleos2k18:latest

deploy:
	eb deploy

run:
	docker-compose up -d

stop:
	docker-compose down