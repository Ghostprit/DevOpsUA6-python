import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_security import SQLAlchemySessionUserDatastore, Security, login_required, current_user
from dotenv import load_dotenv
from database import db
from auth import User, Role

app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "0aedgaii451cef0af8bd6432ec4b317c8999a9f8g77f5f3cb49fb9a8acds51d")
app.config["SECURITY_PASSWORD_SALT"] = os.getenv("SECURITY_PASSWORD_SALT", "ab3d3a0f6984c4f5hkao41509b097a7bd498e903f3c9b2eea667h16")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECURITY_REGISTERABLE"] = True
app.config["SECURITY_SEND_REGISTER_EMAIL"] = False

uri = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = uri

db.init_app(app)

with app.app_context():
    db.create_all()

userDatastore = SQLAlchemySessionUserDatastore(db.session, User, Role)
security = Security(app, userDatastore)

socketio = SocketIO(app)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    if current_user.is_authenticated:
        formatted_msg = f"{current_user.email}: {msg}"
        print('Message: ' + formatted_msg)
        emit('message', formatted_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)