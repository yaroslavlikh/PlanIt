import sqlite3

def init_db():
    conn = sqlite3.connect('tasks.sql')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS tasks(
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT NOT NULL,
        title TEXT NOT NULL,
        start_time TEXT,
        end_time TEXT,
        description TEXT);""")
    conn.commit()
    conn.close()