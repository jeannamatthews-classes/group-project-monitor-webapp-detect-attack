# TODO: implement database logic

posts = [
        {"user": "foobar",
        "body": "foo"},
        {"user": "foobar",
        "body": "foo"},
        {"user": "foobar",
        "body": "foo"},
        {"user": "foobar",
        "body": "foo"},
        {"user": "foobar",
        "body": "foo"},
    ]

def get_posts():
    return posts

def create_post(user: str, body: str):
    posts.append({"user":user,"body":body})