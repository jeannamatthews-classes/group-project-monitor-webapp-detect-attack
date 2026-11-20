# TODO: implement database logic

posts = []

def get_posts():
    return posts

def create_post(user: str, body: str):
    posts.append({"user":user,"body":body})