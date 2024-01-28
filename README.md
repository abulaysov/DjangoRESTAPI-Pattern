## Django REST API Pattern

___

### Requirements:
- Docker
- docker-compose
___

### Usage tools:

```
Python == 3.10
Django == 4.2 LTS
drf == 3.14
PostgreSQL == 14
```
___
### Type checker tools:
```
black
flake8
isort
mypy
```
___
### Commands for management project:
```
make local_up - Build and up project
make local_down - Stop and delete docker containers
make lint - Check linters
make format - Format code with using black and isort
make test - Run tests
make shell - Get into shell of web container
```
___
### Project's structure:
```
├── .github
│   └── workflows
│       └── test_lint.yml
├── configs
│   ├── management
│   │   ├── __init__.py
│   │   └── commands
│   │       ├── __init__.py
│   │       └── wait_for_db.py
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── docs
├── users
│    ├── __init__.py
│    ├── admin.py
│    ├── api
│    │   ├── __init__.py
│    │   └── v1
│    │       ├── __init__.py
│    │       ├── serializers
│    │       │   └── __init__.py
│    │       ├── filters.py
│    │       ├── permissions.py
│    │       ├── routers.py
│    │       └── views.py
│    ├── apps.py
│    ├── migrations
│    │   ├── 0001_initial.py
│    │   └── __init__.py
│    ├── models
│    │   ├── __init__.py
│    │   └── user.py
│    ├── services
│    │   ├── __init__.py
│    │   └── user_create.py
│    ├── tests
│    │   ├── __init__.py
│    │   └── factories.py
│    └── views.py
├── .gitignore
├── conftest.py
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── manage.py
├── poetry.lock
├── pyproject.toml
├── README.md
└── setup.cfg

```