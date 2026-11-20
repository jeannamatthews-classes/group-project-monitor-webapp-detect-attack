from flask import Flask, render_template

app = Flask(__name__)

"""
Store posts in db as
user (fk -> users.user), date, content, id, parent (fk -> posts.id or NULL)

Store users in db as
user (pk), password

Send to posts page as list of posts, where post has list of replies
only posts with null parent are top level
"""

@app.route("/")
def main_page():
    posts = [
        {"user": "foobar",
        "body": "foo",
        "replies":[{"user": "foobar",
        "body": "foo"},{"user": "foobar",
        "body": "foo"}]},
        {"user": "foobar",
        "body": "foo",
        "replies":[{"user": "foobar",
        "body": "foo"},{"user": "foobar",
        "body": "foo"}]},
    ]

    return render_template("posts.html", posts=posts)

app.run()