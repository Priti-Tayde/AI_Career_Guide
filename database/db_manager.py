import sqlite3

DB_NAME = "career_guide.db"

def register_user(username, password):
    # insert user into database
    pass

def login_user(username, password):
    # validate user
    pass
   

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT
        )
    """ )

    conn.commit()
    conn.close()

    print("Tables created")

def save_resume_analysis(user_id, resume_text, analysis):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
         INSERT INTO resume_analysis
         (user_id, resume_text, analysis)
        VALUES (?, ?, ?)
     """, (user_id, resume_text, analysis))

    conn.commit()
    conn.close()  