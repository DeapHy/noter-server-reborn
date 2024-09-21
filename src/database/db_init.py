from src.database.db_helpers import DatabaseConnection, with_db_connection

# Переписать на модели (SQLAlchemy например)
@with_db_connection
def init_database(db: DatabaseConnection, payload: dict = {}):
    print(db.cursor)
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS user (
                        id INTEGER NOT NULL,
                        login VARCHAR(30) NOT NULL,
                        salt VARCHAR(32) NOT NULL,
                        hash VARCHAR(60) NOT NULL,
                        display_name VARCHAR(50) NOT NULL,

                        PRIMARY KEY(id)
                        )""")
    
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS session (
                        id INTEGER NOT NULL,
                        userid INTEGER NOT NULL,
                        is_opened INTEGER NOT NULL,

                        PRIMARY KEY(id),
                        FOREIGN KEY(userid) REFERENCES user(id)
                        )""")
    
    db.cursor.execute("""CREATE TABLE IF NOT EXISTS note (
                        id INTEGER NOT NULL,
                        userid INTEGER NOT NULL,
                        created_at VARCHAR(15) NOT NULL,
                        title VARCHAR(50) NOT NULL,
                        contents VARCHAR(250) NOT NULL,

                        PRIMARY KEY(id),
                        FOREIGN KEY(userid) REFERENCES user(id)
                        )""")
    
    db.connection.commit()
