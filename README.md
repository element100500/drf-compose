# drf-compose

## 🐳 Requirements

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

We highly recommend to use [Docker Desktop](https://www.docker.com/products/docker-desktop), which contains Engine and Compose out of the box.

## ⚙️ Setup
In project root create `.env` file with the following contents:

    COMPOSE_PROJECT_NAME=myproject
    COMPOSE_FILE=docker-compose.dev.yml

## 🏗️ Development

Running development server:

    docker-compose up

Please note `docker-compose.dev.yml` is **development-only** configuration with development-only features like hot reloading and cannot be used in production.

## 🚀 Deployment

Edit `.env` file to use Docker Compose production config:

    COMPOSE_FILE=docker-compose.dev.yml

Set server environment variables in `server/.env` file:

    DB_HOST=db
    ALLOWED_HOSTS=localhost
    CORS_ALLOWED_ORIGINS=localhost

Run composer as daemon:

    docker-compose up -d

(Optional) Collect static files:

    docker-compose exec server python manage.py collectstatic --no-input

(Optional) Create superuser:

    docker-compose exec server python manage.py createsuperuser

