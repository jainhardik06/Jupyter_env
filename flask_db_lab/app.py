from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "students.db"


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                course TEXT NOT NULL
            )
            """
        )


@app.route("/")
def home():
    return render_template("form.html")


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    age = request.form.get("age", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not age or not course:
        return "All fields are required. <a href='/'>Go Back</a>", 400

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
            (name, int(age), course),
        )

    return redirect(url_for("students"))


@app.route("/students")
def students():
    with sqlite3.connect(DB_NAME) as conn:
        data = conn.execute("SELECT * FROM students").fetchall()
    return render_template("display.html", data=data)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
