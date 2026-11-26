from flask import make_response
from flask import Flask, render_template, request, redirect
import bbs.posts as posts
import bbs.users as users
from bbs.db import init_db

db = init_db()

app = Flask(__name__)

@app.route("/")
def main_page():
    p = posts.get_posts(db)
    u = users.validate_user_cookie(request,db)
    return render_template("home.html", posts=p, user=u)

@app.route("/login")
def login_page():
    user = request.args.get("user")
    paswd = request.args.get("paswd")
    if user is not None and paswd is not None:
        if users.check_auth(user,paswd,db):
            r = make_response(redirect("/"))
            r.set_cookie("username",user)
            r.set_cookie("password",paswd)
            return r
        else:
            # When user enters invalid credentials
            return render_template("login.html", try_again = True)
    else:
        return render_template("login.html", try_again = False)

@app.route("/logout")
def logout_page():
    r = make_response(redirect("/"))
    r.delete_cookie("username")
    r.delete_cookie("password")
    return r

@app.route("/enroll")
def enroll_page():
    user = request.args.get("user")
    paswd = request.args.get("paswd")
    if user is not None and paswd is not None:
        if users.create_user(user,paswd,db):
            r = make_response(redirect("/"))
            r.set_cookie("username",user)
            r.set_cookie("password",paswd)
            return r
        else:
            # If name is already in use
            return render_template("enroll.html", try_again = True)
    else:
        return render_template("enroll.html", try_again = False)

@app.route("/post")
def post_page():
    content = request.args.get("content")
    if content is not None:
        user = users.validate_user_cookie(request,db)
        if user is None:
            return redirect("/login")
        posts.create_post(user, content, db)
        return redirect("/")
    else:
        return render_template("post.html")

app.run(host="0.0.0.0",port=5000)