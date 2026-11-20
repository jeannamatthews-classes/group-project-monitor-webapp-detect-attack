# TODO: implement
from flask import request


def create_user(username: str, password: str):
    pass

def check_auth(username: str, password: str) -> bool:
    # check if a username+password combination is valid
    return True

def validate_user_cookie(r: request):
    # return username based on cookie, and only if it is a valid login
    # if invalid or no user cookie, return none
    return "user"