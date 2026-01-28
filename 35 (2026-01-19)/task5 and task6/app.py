from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import sqlite3

app = Flask(__name__)
api = Api(app)

DATABASE = "task.db"
app.config["JWT_SECRET_KEY"] = "test_key"
jwt = JWTManager(app)

def getDbConnection():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, quantity INTEGER)")
    conn.commit()
    conn.close()

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        if data["username"] == "admin" and data["password"] == "password":
            access_token = create_access_token(identity={"username": data["username"]})
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401

class Item(Resource):
    @jwt_required()
    def get(self, item_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items WHERE id=?", (item_id,))
        item = cursor.fetchone()
        conn.close()
        if item:
            return {"id": item[0], "name": item[1], "quantity": item[2]}, 200
        return {"message": "Item not found"}, 404
    
    @jwt_required()
    def post(self):
        data = request.get_json()
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO items (name, quantity) VALUES (?, ?)", (data["name"], data["quantity"]))
        conn.commit()
        item_id = cursor.lastrowid
        conn.close()
        return {"id": item_id, "name": data["name"], "quantity": data["quantity"]}, 201
    
    @jwt_required()
    def put(self, item_id):
        data = request.get_json()
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("UPDATE items SET name=?, quantity=? WHERE id=?", (data["name"], data["quantity"], item_id))
        conn.commit()
        conn.close()
        return {"message": "Item updated"}, 200
    
    @jwt_required()
    def delete(self, item_id):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM items WHERE id=?", (item_id,))
        conn.commit()
        conn.close()
        return {"message": "Item deleted"}, 200

api.add_resource(UserLogin, "/login")
api.add_resource(Item, "/item", "/item/<int:item_id>")

if __name__ == '__main__':
    getDbConnection()
    app.run(debug=True)