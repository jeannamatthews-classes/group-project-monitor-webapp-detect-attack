from flask import Flask, render_template, request, redirect
import bbs.posts as posts
import bbs.users as users

app = Flask(__name__)

@app.route("/")
def main_page():
    p = posts.get_posts()
    return render_template("home.html", posts=p)

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

@app.route("/post")
def post_page():
    content = request.args.get("content")
    if content is not None:
        user = users.validate_user_cookie(request)
        if user is None:
            return redirect("/login")
        posts.create_post(user, content)
        return redirect("/")
    else:
        return render_template("post.html")

app.run()