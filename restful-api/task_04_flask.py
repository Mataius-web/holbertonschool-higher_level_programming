#!/usr/bin/python3
"""Simple Flask API."""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Ne pas ajouter de données de test pour le checker
users = {}


@app.route("/")
def home():
    """Home route."""
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """Status route."""
    return "OK"


@app.route("/data")
def get_data():
    """Return all usernames."""
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """Return a user by username."""
    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user."""

    try:
        data = request.get_json()
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if username is None:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201


if __name__ == "__main__":
    app.run()
