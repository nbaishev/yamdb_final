# Проект YaMDb

## Автор:

💻 [nbaishev](https://github.com/nbaishev)

![Alt-текст](https://boxboat.com/2017/06/28/whats-new-in-docker-17-06/featured.png "Кит по имени Docker")


![yamdb_workflow](https://github.com/nbaishev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание проекта REST API для YaMDb

Создан на основе фреймворка [Django REST Framework (DRF)](https://github.com/ilyachch/django-rest-framework-rusdoc)


Проект YaMDb собирает отзывы пользователей о произведениях. Работы разделены на категории: «Книги», «Фильмы», «Музыка». [Ссылка](https://github.com/nbaishev/api_yamdb) на репозиторий с проектом.

____

## Технологии:

- Python 3
- DRF (Django REST framework)
- Django ORM
- Docker
- Gunicorn
- Nginx
- Django 3.2
- PostgreSQL
- GIT
___
## Запуск проекта 🚀

1. Клонировать репозиторий и перейти в него в командной строке:
```bash 
https://github.com/nbaishev/yamdb_final.git

cd yamdb_final
```
2. Перейти в директорию  ```cd infra``` и создать файл .env, заполнить его по следующему примеру:

```
DB_ENGINE= # указываем базу данных
DB_NAME= # задаем имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД
DB_HOST= # название сервиса (контейнера)
DB_PORT= # порт для подключения к БД
SECRET_KEY= # установить секретный ключ
DEBUG=False
ALLOWED_HOSTS= # указать разрешенные хосты
```
4. Установка и запуск приложения в контейнерах (контейнер web загружактся из DockerHub):
```bash 
docker-compose up -d
```

5. Запуск миграций, создание суперюзера, сбор статики и заполнение БД:
```bash 
docker-compose exec web python manage.py migrate

docker-compose exec web python manage.py createsuperuser

docker-compose exec web python manage.py collectstatic --no-input 

docker-compose exec web python manage.py loaddata fixtures.json
```
Документация к проекту
----------
Документация для API после установки доступна по адресу 

```http://127.0.0.1/redoc/```

[Пример успешно запущенного проекта](http://158.160.100.90/api/v1/)