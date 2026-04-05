from flask import Flask, render_template, request
import os
import sqlite3
from predict import predict_image, detect_severity

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# 🔥 Initialize Database
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS complaints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            issue TEXT,
            priority TEXT,
            status TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()


# 🔥 Priority Function
def get_priority(issue):
    if issue == "pothole":
        return "High"
    else:
        return "Medium"


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Upload Route
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # AI Prediction
        result = predict_image(filepath)

        # Severity
        severity = detect_severity(filepath)

        # Priority
        priority = get_priority(result)

        # Save to DB
        conn = sqlite3.connect("database.db")
        c = conn.cursor()

        c.execute(
            "INSERT INTO complaints (filename, issue, priority, status) VALUES (?, ?, ?, ?)",
            (file.filename, f"{result} ({severity})", priority, "Pending")
        )

        conn.commit()
        conn.close()

        return f"Issue: {result} | Priority: {priority} | Severity: {severity}"

    return "No file uploaded"


# 🔥 Admin Dashboard
@app.route("/admin")
def admin():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT * FROM complaints")
    data = c.fetchall()

    conn.close()

    return render_template("admin.html", data=data)


# 🔥 Status Update Route
@app.route("/update_status/<int:id>")
def update_status(id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("UPDATE complaints SET status='Resolved' WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return "<h3>Status Updated!</h3><a href='/admin'>Go Back</a>"


# 🔥 Analytics Route
@app.route("/analytics")
def analytics():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()

    c.execute("SELECT COUNT(*) FROM complaints WHERE issue LIKE 'pothole%'")
    pothole_count = c.fetchone()[0]

    c.execute("SELECT COUNT(*) FROM complaints WHERE issue LIKE 'garbage%'")
    garbage_count = c.fetchone()[0]

    conn.close()

    return render_template("analytics.html",
                           pothole=pothole_count,
                           garbage=garbage_count)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)