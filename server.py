from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)
app.secret_key = " 8891techa0128"

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
    data = {"id": user_id}
    return render_template("edit_user.html", user = User.get_one(data))

@app.route("/update-user", methods = ["POST"])
def p_edit_user():
    User.update(request.form)
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)