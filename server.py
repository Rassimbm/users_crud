from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)
app.secret_key = " 8891techa0128"

@app.route("/")
def index():
    return render_template("index.html", users = User.get_all())

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
    
@app.route("/show-user/<int:user_id>")
def show_user(user_id):
    return render_template("show_user.html", user = User.get_one(user_id))
    
if __name__ == "__main__":
    app.run(debug=True)