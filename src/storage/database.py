import sqlite3
from pathlib import Path

class Database:

    def __init__(self, db_path="data/curiosity_engine.db"):
        Path("data").mkdir(exist_ok=True)

        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
    
    def execute(self, query, params = ()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor
    
    def executemany(self, query, params):
        cursor = self.conn.cursor()
        cursor.executemany(query, params)
        self.conn.commit()
        return cursor
    
    def initialize_schema(self):

        self.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            id INTEGER PRIMARY KEY,
            url TEXT UNIQUE,
            title TEXT,
            status_code INTEGER,
            html TEXT,
            crawled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS links (
            id INTEGER PRIMARY KEY,
            source_url TEXT,
            target_url TEXT,
            UNIQUE(source_url, target_url)
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS frontier (
            url TEXT PRIMARY KEY,
            depth INTEGER,
            priority REAL
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS domains (
            domain TEXT PRIMARY KEY,
            last_crawled TIMESTAMP
        )
        """)