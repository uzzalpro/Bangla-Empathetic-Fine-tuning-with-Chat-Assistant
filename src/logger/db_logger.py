import sqlite3, json
from datetime import datetime

class ExperimentLogger:
    def __init__(self, db_path="logs/experiments.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS LLAMAExperiments (
            id INTEGER PRIMARY KEY,
            model_name TEXT,
            lora_config TEXT,
            train_loss REAL,
            val_loss REAL,
            metrics TEXT,
            timestamp TEXT
        )
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS GeneratedResponses (
            id INTEGER PRIMARY KEY,
            experiment_id INTEGER,
            input_text TEXT,
            response_text TEXT,
            timestamp TEXT
        )
        """)
        conn.commit()
        conn.close()

    def log_experiment(self, model_name, lora_cfg, metrics):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("""
        INSERT INTO LLAMAExperiments VALUES (NULL,?,?,?,?,?,?)
        """, (
            model_name,
            json.dumps(lora_cfg),
            metrics.get("train_loss"),
            metrics.get("val_loss"),
            json.dumps(metrics),
            datetime.utcnow().isoformat()
        ))
        conn.commit()
        conn.close()
