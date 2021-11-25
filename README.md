# Django REST framework + Docker Compose boilerplate

## 🔥 Features

- Split settings (dev/prod)
- User model for extend
- API auth (Bearer token)
- API documentation (OpenAPI Schema, Swagger, ReDoc)
- Minimal Nginx config

## 🐳 Requirements

- [Docker Engine](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)

We highly recommend to use [Docker Desktop](https://www.docker.com/products/docker-desktop), which contains Engine and Compose out of the box.

## ⚙️ Configuration
In project root create `.env` file with the following contents:

    COMPOSE_PROJECT_NAME=myproject
    COMPOSE_FILE=docker-compose.dev.yml

Please note `docker-compose.dev.yml` is **development-only** configuration with development-only features like hot reloading and cannot be used in production.

## 🏗️ Development

Start development server:

    docker-compose up

Check http://localhost:8000/admin/

## 🚀 Deploy

Edit `.env` file to use composer production config:

    COMPOSE_FILE=docker-compose.dev.yml

Set server environment variables in `server/.env` file:

    SECRET_KEY=my-strong-secret-key
    DEBUG=
    DB_HOST=db
    ALLOWED_HOSTS=mydomain.com
    CORS_ALLOWED_ORIGINS=mydomain.com

Run composer as daemon:

    docker-compose up -d

Check http://mydomain.com/admin/

### Optional

Collect static files:

    docker-compose exec server python manage.py collectstatic --no-input

Create superuser:

    docker-compose exec server python manage.py createsuperuser

