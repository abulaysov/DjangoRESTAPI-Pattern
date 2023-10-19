FROM python:3.10-slim

WORKDIR /app


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ARG DEV=false

RUN pip install --upgrade pip && pip install "poetry==1.4.1"

RUN apt-get update && apt-get install -y build-essential libpq-dev curl make git tzdata

ENV TZ=Europe/Moscow

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    if [ "$DEV" = "true" ]; then \
      poetry install --no-interaction --no-ansi ; \
    else poetry install --no-interaction --no-ansi --without dev ; \
    fi

COPY . .

RUN adduser --disabled-password --no-create-home john-doe

RUN python /app/manage.py collectstatic --noinput

USER john-doe
