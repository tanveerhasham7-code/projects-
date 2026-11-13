"""Small SQLite audit store for the educational single-instance deployment."""
import json
import os
import sqlite3
from datetime import datetime, timezone

def connect(path: str):
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    db = sqlite3.connect(path)
    db.execute("""CREATE TABLE IF NOT EXISTS cases (
        fingerprint TEXT PRIMARY KEY,
        received_at TEXT NOT NULL,
        alert_id TEXT,
        agent_name TEXT,
        severity TEXT NOT NULL,
        risk_score INTEGER NOT NULL,
        notify_analyst INTEGER NOT NULL,
        decision_json TEXT NOT NULL,
        ai_assessment_json TEXT NOT NULL DEFAULT '{}',
        notification_status TEXT NOT NULL
    )""")
    # Lightweight migration for databases created by an earlier project version.
    columns = {row[1] for row in db.execute("PRAGMA table_info(cases)")}
    if "ai_assessment_json" not in columns:
        db.execute("ALTER TABLE cases ADD COLUMN ai_assessment_json TEXT NOT NULL DEFAULT '{}'")
    return db

def save_case(path: str, fingerprint: str, event: dict, decision: dict,
              notification_status: str, ai_result: dict | None = None) -> bool:
    db = connect(path)
    try:
        cursor = db.execute(
            """INSERT OR IGNORE INTO cases
            (fingerprint, received_at, alert_id, agent_name, severity, risk_score,
             notify_analyst, decision_json, ai_assessment_json, notification_status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (fingerprint, datetime.now(timezone.utc).isoformat(), event.get("alert_id"),
             event.get("agent_name"), decision["severity"], decision["risk_score"],
             int(decision["notify_analyst"]), json.dumps(decision),
             json.dumps(ai_result or {}), notification_status),
        )
        db.commit()
        return cursor.rowcount == 1
    finally:
        db.close()

def update_notification(path: str, fingerprint: str, status: str) -> None:
    db = connect(path)
    try:
        db.execute("UPDATE cases SET notification_status=? WHERE fingerprint=?", (status, fingerprint))
        db.commit()
    finally:
        db.close()
