from dotenv import load_dotenv
import os
import sqlite3

# Load .env variables
load_dotenv()

# Pfad zur SQLite-Datei (Standard: db.sqlite3 im Projektordner)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.getenv("DB_PATH", os.path.join(BASE_DIR, "db.sqlite3"))
SCHEMA_PATH = os.path.join(BASE_DIR, "db", "TODOS.sql")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    # Zeilen als Dict-ähnliche Objekte liefern (row["spalte"])
    conn.row_factory = sqlite3.Row
    # SQLite prüft Fremdschlüssel nur, wenn es explizit eingeschaltet wird
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    """Erstellt alle Tabellen (und Beispieldaten) aus db/TODOS.sql neu."""
    with open(SCHEMA_PATH, encoding="utf-8") as f:
        schema = f.read()
    conn = get_conn()
    try:
        conn.executescript(schema)
        conn.commit()
    finally:
        conn.close()
    print("Datenbank initialisiert:", DB_PATH)


# Beim ersten Start automatisch die Datenbank anlegen
if not os.path.exists(DB_PATH):
    init_db()


# DB-Helper
def db_read(sql, params=None, single=False):
    conn = get_conn()
    try:
        cur = conn.execute(sql, params or ())

        if single:
            # liefert EIN Dict oder None
            row = cur.fetchone()
            row = dict(row) if row else None
            print("db_read(single=True) ->", row)   # DEBUG
            return row
        else:
            # liefert Liste von Dicts (evtl. [])
            rows = [dict(r) for r in cur.fetchall()]
            print("db_read(single=False) ->", rows)  # DEBUG
            return rows

    finally:
        conn.close()


def db_write(sql, params=None):
    conn = get_conn()
    try:
        conn.execute(sql, params or ())
        conn.commit()
        print("db_write OK:", sql, params)  # DEBUG
    finally:
        conn.close()


# "python db.py" setzt die Datenbank auf den Ausgangszustand zurück
if __name__ == "__main__":
    init_db()
