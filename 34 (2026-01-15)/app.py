from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

app = Flask(__name__)
app.secret_key = "TESTKEY"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

users = {"admin": {"password": "password"}}

class User(UserMixin):
    def __init__(self, id):
        self.id = id
    
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and users[username]["password"] == password:
            user = User(username)
            login_user(user)
            flash("Logged in successfully.")
            return redirect(url_for("protected"))
        else:
            flash("Invalid credentials.")
    return render_template("login.html")

@app.route("/protected")
@login_required
def protected():
    return f"Hello, {current_user.id}! This is a protected page."

if __name__ == "__main__":
    app.run(debug=True)