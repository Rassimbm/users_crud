from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User

@app.route("/")
def index():
    return render_template("index.html", users = User.get_all())

@app.route("/show-user/<int:user_id>")
def show_user(user_id):
    data = {
                "id": user_id
                                }
    return render_template("show_user.html", user = User.get_one(data))

@app.route("/add-user", methods = ["GET", "post"])
def add_user():
    if request.method == "GET":
        return render_template("new_user.html")
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"]
        }
        User.save(data)
        return redirect("/")
    
@app.route("/edit-user/<int:user_id>")
def r_edit_user(user_id):
    data = {
                "id": user_id
                                }
    return render_template("edit_user.html", user = User.get_one(data))

@app.route("/update-user", methods = ["POST"])
def p_edit_user():
    User.update(request.form)
    return redirect("/")

@app.route("/delete-user/<int:user_id>")
def delete(user_id):
    data = {
                "id": user_id
                                }
    User.delete(data)
    return redirect("/")