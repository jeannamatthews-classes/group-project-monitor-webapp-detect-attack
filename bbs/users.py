# TODO: implement
from flask import request
import psycopg2


def create_user(username: str, password: str, db: psycopg2.connection):
    pass

def check_auth(username: str, password: str, db: psycopg2.connection) -> bool:
    # check if a username+password combination is valid
    return True

def validate_user_cookie(r: request, db: psycopg2.connection):
    # return username based on cookie, and only if it is a valid login
    # if invalid or no user cookie, return none
    return "user"