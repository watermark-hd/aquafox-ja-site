import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, send_from_directory, g

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database.db"
XPI_DIR = BASE_DIR / "static" / "downloads"
XPI_FILENAME = "aquafox-ja.xpi"

app = Flask(__name__)


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
    return g.db


@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS downloads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            downloaded_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index():
    db = get_db()
    count = db.execute("SELECT COUNT(*) FROM downloads").fetchone()[0]
    return render_template("index.html", download_count=count)


@app.route("/download")
def download():
    db = get_db()
    db.execute(
        "INSERT INTO downloads (downloaded_at) VALUES (?)",
        (datetime.utcnow().isoformat(),),
    )
    db.commit()
    return send_from_directory(XPI_DIR, XPI_FILENAME, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
