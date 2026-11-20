# TODO: implement
from flask import request


def create_user(username: str, password: str):
    pass

def check_auth(username: str, password: str) -> bool:
    return True

def get_user_cookie(r: request):
    # return username based on cookie
    return "user"