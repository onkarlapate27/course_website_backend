import os

class Settings:
    mongodb_host_name = os.environ.get("MONGO_HOST_NAME", "localhost")
    mongodb_port = os.environ.get("MONGO_PORT", "27017")
    db_name = os.environ.get("DB_NAME", "course_database")

    mongo_connection_string: str = f"mongodb://{mongodb_host_name}:{mongodb_port}/"
    database_name: str = f"{db_name}"

settings = Settings()
