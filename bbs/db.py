import psycopg2

def init_db():
    db = psycopg2.connect(
        dbname="bbs",
        user="postgres",
        password="postgres",
        host="postgres"
    )

    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users 
    (
        id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        username VARCHAR(255) UNIQUE,
        password VARCHAR(255)
    );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS posts 
    (
        id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        user INTEGER,
        content TEXT,
        FOREIGN KEY (user) REFERENCES users(id)
    );""")

    return db