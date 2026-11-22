import psycopg2
from time import sleep

def init_db():
    sleep(1) # db is slow to start up

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
        uid INTEGER,
        content TEXT,
        FOREIGN KEY (uid) REFERENCES users(id)
    );""")

    # TODO: temporary remove this
    cur.execute("INSERT INTO users (username,password) VALUES ('user','user');")
    db.commit()
    cur.close()
    return db