from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Hardcoded credentials (Bad practice)
ADMIN_USER = "admin"
ADMIN_PASS = "admin123"

# Route for login
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Vulnerable to SQL Injection!
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            return f"Welcome, {username}!"
        else:
            return "Login failed!"
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

