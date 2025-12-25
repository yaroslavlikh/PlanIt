import sqlite3

def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor("tasks.db")
    cursor.execute(
        """
        CREATE TABLE IF NOT EXIST tasks(
        id INTEGTER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGTER NOT NULL,
        title TEXT NOT NULL,
        start_time TEXT,
        end_time TEXT,
        description TEXT
        )
        """
    )
    conn.commit()
    conn.close()