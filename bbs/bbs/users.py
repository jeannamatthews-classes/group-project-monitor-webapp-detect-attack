from flask import request
import psycopg2


def create_user(username: str, password: str, db: psycopg2.connection):
    cur = db.cursor()
    try:
        cur.execute("INSERT INTO users (username, password) VALUES (%s,%s)",(username,password))
        rc = True
    except psycopg2.errors.UniqueViolation:
        rc = False
    db.commit()
    cur.close()
    return rc

def check_auth(username: str, password: str, db: psycopg2.connection) -> bool:
    # check if a username+password combination is valid
    cur = db.cursor()
    cur.execute("SELECT password FROM users WHERE username = %s",(username,))
    real_passwd = cur.fetchone()
    if real_passwd is None:
        return False
    else:
        real_passwd = real_passwd[0]
    cur.close()
    if password == real_passwd:
        return True
    else: 
        return False

def validate_user_cookie(r: request, db: psycopg2.connection):
    # return username based on cookie, and only if it is a valid login
    # if invalid or no user cookie, return none
    user = r.cookies.get("username")
    paswd = r.cookies.get("password")
    if check_auth(user,paswd,db):
        return user
    else:
        return None