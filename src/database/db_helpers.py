from dataclasses import dataclass
import sqlite3

# Проверка на единственное активное подключение к БД
def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

# Модель коннектора к БД
@singleton
@dataclass
class DatabaseConnection():
    connection: sqlite3.Connection
    cursor: sqlite3.Cursor

# Подключение к БД
def with_db_connection(func):
    def wrapper(payload: dict = {}):
        try:
            with sqlite3.connect('src/database/notes.db') as connection:
                cursor = connection.cursor()
                db_connection_instance = DatabaseConnection(
                    connection=connection,
                    cursor=cursor
                )
                return func(db_connection_instance, payload)
        except Exception as e:
            print(f"Error connecting to database {e}")
            return "error"
    return wrapper