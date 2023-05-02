# yamdb_final
yamdb_final
![yamdb_workflow](https://github.com/nbaishev/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
Перейти в директорию  ```cd infra``` и создать файл .env, заполнить его по следующему примеру:

```
DB_ENGINE= # указываем, что работаем с postgresql
DB_NAME= # имя базы данных
POSTGRES_USER= # логин для подключения к базе данных
POSTGRES_PASSWORD= # пароль для подключения к БД (установите свой)
DB_HOST= # название сервиса (контейнера)
DB_PORT= # порт для подключения к БД
```