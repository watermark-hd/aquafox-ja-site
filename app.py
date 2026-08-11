import sqlite3
from datetime import datetime
from pathlib import Path

from flask import Flask, render_template, send_from_directory, g, abort

from apps import APPS, APPS_BY_SLUG

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database.db"
XPI_DIR = BASE_DIR / "static" / "downloads"

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
            app_slug TEXT NOT NULL,
            downloaded_at TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


init_db()


def get_download_counts():
    db = get_db()
    rows = db.execute(
        "SELECT app_slug, COUNT(*) FROM downloads GROUP BY app_slug"
    ).fetchall()
    counts = {app["slug"]: 0 for app in APPS}
    counts.update(dict(rows))
    return counts


@app.route("/")
def top():
    return render_template(
        "top.html", apps=APPS, download_counts=get_download_counts()
    )


@app.route("/apps/<slug>")
def app_detail(slug):
    if slug not in APPS_BY_SLUG:
        abort(404)
    return render_template(
        f"apps/{slug}.html",
        app=APPS_BY_SLUG[slug],
        download_count=get_download_counts()[slug],
    )


@app.route("/download/<slug>")
def download(slug):
    if slug not in APPS_BY_SLUG:
        abort(404)
    db = get_db()
    db.execute(
        "INSERT INTO downloads (app_slug, downloaded_at) VALUES (?, ?)",
        (slug, datetime.utcnow().isoformat()),
    )
    db.commit()
    return send_from_directory(XPI_DIR, APPS_BY_SLUG[slug]["filename"], as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
