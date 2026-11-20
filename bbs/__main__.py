from flask import Flask, render_template, request, redirect
import bbs.posts as posts
import bbs.users as users

app = Flask(__name__)

""" 
Store posts in db as
user (fk -> users.user), date, content

Store users in db as
user (pk), password
"""

@app.route("/")
def main_page():
    p = posts.get_posts()
    return render_template("posts.html", posts=p)

@app.route("/login")
def login_page():
    user = request.args.get("user")
    paswd = request.args.get("paswd")
    if user is not None and paswd is not None:
        if users.check_auth(user,paswd):
            # TODO: set user cookie
            return redirect("/")
        else:
            # When user enters invalid credentials
            return render_template("login.html", try_again = True)
    else:
        return render_template("login.html", try_again = False)

app.run()