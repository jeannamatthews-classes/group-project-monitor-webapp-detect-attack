import psycopg2

def get_posts(db: psycopg2.connection):
    cur = db.cursor()
    cur.execute("SELECT uid,content FROM posts;")
    raw_posts = cur.fetchall()
    posts = []
    for post in raw_posts:
        uid = post[0]
        content = post[1]
        cur.execute(f"SELECT (username) FROM users WHERE id = {uid};")
        username = cur.fetchone()[0]
        posts.append({"user":username, "body": content})
    db.commit()
    cur.close()
    return posts

def create_post(user: str, body: str, db: psycopg2.connection):
    cur = db.cursor()
    cur.execute(f"SELECT (id) FROM users WHERE username = '{user}';")
    uid = cur.fetchone()[0]
    cur.execute(f"INSERT INTO posts (uid, content) VALUES ({uid},'{body}');")
    db.commit()
    cur.close()