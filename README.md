# Docker + Django + Nginx + PostgreSQL + Gunicorn

This is a simple Django app to example how to get started with all these tools, the app get show data from a postgresql database, which is a list of recommends books to read.
The only goal of this app is to serve as an example of the initial configurations to be made when you are deploying using the mentioned stack.

## Getting Started

To see the example running you need to have docker and docker-compose on your machine then follow next steps

```
$ git clone git@github.com:bayocr/example-docker-django.git
$ cd example-docker-django 
```
Now you can customize environment variables on envs/app.env and envs/postgres.env (these environment variables will be used by docker when start containers), then you can run containers

```
$ docker-compose up --build -d
$ docker-compose exec app python manage.py migrate
$ docker-compose exec app python manage.py loaddata author book
```

Now access to http//:localhost or the host your defined in ALLOWED_HOSTS variable into the file app.env


