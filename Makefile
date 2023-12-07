docker-build-bot:
	docker build --tag "astoria-bot" . -f Dockerfile.bot

docker-run-bot:
	docker run --rm -it  astoria-bot:latest

docker-build-db:
	docker build --tag "astoria-db" . -f Dockerfile.db

docker-run-db:
	docker run --rm -it  astoria-db:latest

start:
	python3 bot/bot.py

start-mysql:
	sudo service mysql start
	mysql -u root -p

stop-mysql:
	sudo service mysql stop

pylint-all:
	pylint bot/*

black:
	black .

black-check:
	black --check .