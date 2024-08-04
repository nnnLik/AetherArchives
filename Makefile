up:
	docker compose up -d
	
up-build:
	docker compose up -d --build

up-log:
	docker compose up

down:
	docker compose down

log:
	docker compose logs -f -n 100

log-core:
	docker logs core-server -f -n 100
