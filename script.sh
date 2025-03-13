#!/bin/bash

echo "Starting the application"

echo "Running migrations"

alembic revision --autogenerate -m "Initial $(date)"
alembic upgrade head


echo "Running Hypercorn server"
hypercorn --reload -c /app/hypercorn.toml src.main:app