FROM python:3.8-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app


RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip && pip install pipenv

ADD Pipfile Pipfile.lock ./

RUN pipenv install --system

ADD app .
ADD envs/app.env ./.env
ADD config/gunicorn/gunicorn.conf.py .

RUN python manage.py collectstatic

EXPOSE 8000

CMD [ "gunicorn", "-c", "gunicorn.conf.py", "app.wsgi"]
