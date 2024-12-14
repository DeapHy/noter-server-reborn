from src.database.db_helpers import DatabaseConnection, with_db_connection, with_user_exists
from uuid import uuid4
from datetime import datetime

# Создание аккаунта
@with_db_connection
def create_user_account(db: DatabaseConnection, payload: dict) -> None:
    db.cursor.execute(f'INSERT INTO user(login, salt, hash, display_name) values (?, ?, ?, ?)', (payload["login"], payload["salt"], payload["hash"], payload["display_name"]))
    db.connection.commit()
    return {
        "Success": True,
        "detail": {
            
        }
    }

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
@with_db_connection
@with_user_exists
@with_active_session
def set_nickname(db: DatabaseConnection, user: list, payload: dict):
    db.cursor.execute("UPDATE user SET display_name=? WHERE id=?", (payload["new_display_name"], user[0]))
    db.connection.commit()
    return {
        "Success": True,
        "detail": {
            "user_id": user[0],
            "new_display_name": payload["new_display_name"]
        }
    }

# Создание новой заметки
@with_db_connection
@with_user_exists
@with_active_session
def create_note(db: DatabaseConnection, user: list, payload: dict):
    db.cursor.execute("INSERT INTO note (userid, created_at, title, contents) VALUES (?, ?, ?, ?)", (user[0], datetime.now(), payload["title"], payload["contents"]))
    db.connection.commit()
    return {
        "Success": True,
        "detail": {
            "user_id": user[0],
            "note": {
                
            }
        }
    }

# Получение списка заметок определенного пользователя
@with_db_connection
@with_user_exists
@with_active_session
def get_all_user_notes(db: DatabaseConnection, user: list, payload: dict):
    result = db.cursor.execute("SELECT * FROM note WHERE user_id=?", (user[0]))
    return {
        "Success": True,
        "detail": {
            "notes": result
        }
    }

# Обновление определенной заметки
@with_db_connection
@with_user_exists
@with_active_session
def update_note(db: DatabaseConnection, user: list, payload: dict):
    db.cursor.execute("UPDATE note SET title=?, contents=? WHERE user_id=?", (payload["title"], payload["contents"], user[0]))
    db.connection.commit
    return {
        "Success": True,
        "detail": {

        }
    }

# Удаление определенной заметки
@with_db_connection
@with_user_exists
@with_active_session
def delete_note(db: DatabaseConnection, user: list, payload: dict):
    db.cursor.execute("DELETE FROM note WHERE id=?", (payload["note_id"]))
    db.connection.commit()
    return {
        "Success": True,
        "detail": {
            "note_id": payload["note_id"]
        }
    }

# Выход с аккаунта
@with_db_connection
@with_user_exists
@with_active_session
def logout(db: DatabaseConnection, user: list, payload: dict):
    db.cursor.execute("UPDATE session SET is_opened=false WHERE userid=?", (user[0]))
    db.connection.commit()
    return {
        "Success": True,
        "detail": {

        }
    }