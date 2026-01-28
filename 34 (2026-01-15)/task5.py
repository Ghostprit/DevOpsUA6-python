from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }

with app.app_context():
    db.create_all()

@app.route("/add", methods=["POST"])
def addUser():
    data = request.get_json()
    new_user = User(name=data["name"], email=data["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.toDict()), 201

@app.route("/display", methods=["GET"])
def displayUsers():
    users = User.query.all()
    return jsonify([user.toDict() for user in users]), 200

@app.route("/seearch/<int:user_id>", methods=["GET"])
def searchUser(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.toDict()), 200

if __name__ == "__main__":
    app.run(debug=True)