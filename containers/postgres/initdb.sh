#!/bin/bash

# For tests, the user must have the CREATEDB permission.
psql -U postgres <<-EOSQL
    CREATE USER nit_user WITH PASSWORD 'password';
    CREATE DATABASE nit_db;
    GRANT ALL PRIVILEGES ON DATABASE "nit_db" TO nit_user;
    ALTER USER nit_user CREATEDB;
EOSQL
