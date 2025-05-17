import os

db_config = {
    "usuario": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "host": os.environ.get("DB_HOST"),
    "puerto": os.environ.get("DB_PORT"),
    "base_datos": os.environ.get("DB_NAME")
}
