from flask import Flask, render_template
# from friend import Friend
app = Flask(__name__)
app.secret_key = " 8891techa0128"

@app.route("/")
def index():
    return render_template("index.tml")

if __name__ == "__main__":
    app.run(debug=True)