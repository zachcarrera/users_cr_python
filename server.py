from flask import Flask, render_template, redirect, request

from users import User

app = Flask(__name__)

# page to show all users in a table
@app.route("/")
@app.route("/users")
def show_all():

    # query the db to get all users
    users = User.get_all()
    return render_template("all_users.html", users = users)


# page with a form to create a new user
@app.route("/users/new")
def new_user():
    return render_template("create_user.html")

# form submission to create user and redirect
@app.route("/create_user", methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug = True)