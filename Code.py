from flask import Flask, request, jsonify

app = Flask(__name__)

# 🟡 Ask user to input initial users before starting the server
users = {}
num_users = int(input("How many users to add? "))

for i in range(1, num_users + 1):
    name = input(f"Enter name for user {i}: ")
    age = int(input(f"Enter age for user {i}: "))
    users[i] = {"name": name, "age": age}

# -----------------------------
# GET: Get user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({"id": user_id, "user": user})
    return jsonify({"error": "User not found"}), 404

# -----------------------------
# POST: Add new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    if not data or "name" not in data or "age" not in data:
        return jsonify({"error": "Missing name or age"}), 400

    new_id = max(users.keys(), default=0) + 1
    users[new_id] = {"name": data["name"], "age": data["age"]}
    return jsonify({"message": "User created", "id": new_id}), 201

# -----------------------------
# PUT: Update user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": users[user_id]})

# -----------------------------
# DELETE: Delete user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": f"User {user_id} deleted"})
    return jsonify({"error": "User not found"}), 404

# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
