# Backend Lab 4

Варіант 2

## Before start

* Run docker-compose up db in first terminal
* Then change `SQLALCHEMY_DATABASE_URI`'s host from db to localhost
* Run flask db migrate
* Then change `SQLALCHEMY_DATABASE_URI`'s host back to db
* Run docker-compose up to start app