import sqlite3
import json
from datetime import datetime, timezone
from typing import List, Dict, Any, Optional
from ..config import settings

def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(settings.DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analyses (
            id TEXT PRIMARY KEY,
            image_filename TEXT NOT NULL,
            plant_name TEXT NOT NULL,
            condition_name TEXT NOT NULL,
            predicted_class TEXT NOT NULL,
            confidence REAL NOT NULL,
            top_predictions TEXT, -- JSON string
            model_name TEXT NOT NULL,
            model_version TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            status TEXT NOT NULL,
            is_healthy INTEGER NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def save_analysis(record: Dict[str, Any]) -> None:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO analyses (
            id, image_filename, plant_name, condition_name,
            predicted_class, confidence, top_predictions,
            model_name, model_version, timestamp, status, is_healthy
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        record["id"],
        record["image_filename"],
        record["plant_name"],
        record["condition_name"],
        record["predicted_class"],
        record["confidence"],
        json.dumps(record.get("top_predictions", [])),
        record["model_name"],
        record["model_version"],
        record.get("timestamp", datetime.now(timezone.utc).isoformat()),
        record.get("status", "completed"),
        1 if record.get("is_healthy") else 0
    ))
    conn.commit()
    conn.close()

def get_all_analyses(limit: int = 100) -> List[Dict[str, Any]]:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM analyses ORDER BY timestamp DESC LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    
    results = []
    for r in rows:
        d = dict(r)
        if d.get("top_predictions"):
            try:
                d["top_predictions"] = json.loads(d["top_predictions"])
            except Exception:
                d["top_predictions"] = []
        d["is_healthy"] = bool(d["is_healthy"])
        results.append(d)
    return results

def clear_all_history() -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM analyses")
    deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return deleted
