
build:
	docker build  . --rm -t app-flask
start:
	docker run --rm -it -e PORT=3000 --name app-flask -p 3000:3000 app-flask