#!/usr/bin/env bash

PG_HOST='localhost'
PG_PORT=5433
PG_USER='django'
PG_PASSWORD='hotelrooms'
PG_DB_NAME='hotelrooms'

docker run -p $PG_PORT:5432 --name pg_hotels_room \
  -e POSTGRES_PASSWORD=$PG_PASSWORD \
  -e POSTGRES_USER=$PG_USER \
  -e POSTGRES_DB=$PG_DB_NAME \
  -v postgres_db:/var/lib/postgresql/data -d postgres
