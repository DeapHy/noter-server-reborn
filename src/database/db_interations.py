from src.database.db_helpers import DatabaseConnection, with_db_connection, with_user_exists
from uuid import uuid4

# Создание аккаунта
@with_db_connection
def create_user_account(db: DatabaseConnection, payload: dict) -> None:
    db.cursor.execute(f'INSERT INTO user(login, salt, hash, display_name) values (?, ?, ?, ?)', (payload["login"], payload["salt"], payload["hash"], payload["display_name"]))
    db.connection.commit()

# Получение One-Time Token
@with_db_connection
def get_ott(db: DatabaseConnection, payload: dict) -> str:
    user_OTT = db.cursor.execute("SELECT salt FROM user WHERE login=?", (payload["login"], )).fetchall()
    if len(user_OTT):
        return user_OTT[0]
    return uuid4()

# Логин с помощью OTT
@with_db_connection
@with_user_exists
def login(db: DatabaseConnection, user: list, payload: dict) -> dict:
    if user[3] == payload["hash"]:
        db.cursor.execute("INSERT INTO session(userid, is_opened) VALUES (?, ?)", (user[0], 1))
        db.connection.commit()
        return {"Success": True, "detail": {"nickname": user[4]}}
    return {"Success": False, "detail": {"reason": "Hash is incorrect"}}

# Установка никнейма

# Создание новой заметки

# Получение списка заметок определенного пользователя

# Обновление определенной заметки

# Удаление определенной заметки

# Выход с аккаунта