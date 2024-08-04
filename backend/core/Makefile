make-and-migrate: makemigrations migrate

makemigrations:
	docker exec -it core-server ./manage.py makemigrations

migrate:
	docker exec -it core-server ./manage.py migrate

shell:
	docker exec -it core-server ./manage.py shell

collectstatic:
	docker exec -it core-server ./manage.py collectstatic
