docker-build-bot:
	docker build --tag "astoria-bot" . -f Dockerfile.bot

docker-run-bot:
	docker run --rm -it  astoria-bot:latest

docker-build-db:
	docker build --tag "astoria-db" . -f Dockerfile.db

docker-run-db:
	docker run -it --name mysql-db --env-file=.env -p 3306:3306 astoria-db:latest

start:
	python3 bot/bot.py

pylint-all:
	pylint bot/*

black:
	black .

black-check:
	black --check .