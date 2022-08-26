start:
	python3 bot/bot.py

start-mysql:
	sudo service mysql start
	mysql -u root -p

stop-mysql:
	sudo service mysql stop