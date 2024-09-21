from src.database.db_helpers import DatabaseConnection, with_db_connection

# Создание аккаунта
@with_db_connection
def create_account(db: DatabaseConnection, payload: dict) -> None:
    db.cursor.execute(f'INSERT INTO user(login, salt, hash, display_name) values (?, ?, ?, ?)', (payload["login"], payload["salt"], payload["hash"], payload["display_name"]))
    db.connection.commit()

# Получение One-Time Token

# Логин с помощью OTT

# Установка никнейма

# Создание новой заметки

# Получение списка заметок определенного пользователя

# Обновление определенной заметки

# Удаление определенной заметки

# Выход с аккаунта