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
            content_hash TEXT,
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

        self.execute("""
        CREATE TABLE IF NOT EXISTS curiosity_scores (
            id INTEGER PRIMARY_KEY,
            url TEXT,
            score REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS concepts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS relationships (
            source TEXT,
            target TEXT,
            weight INTEGER DEFAULT 1,
            UNIQUE(source, target)
        )
        """)

        self.execute("""
        CREATE TABLE IF NOT EXISTS discoveries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            score REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
        """)

        self.execute("""
        CREATE INDEX IF NOT EXISTS idx_pages_url ON pages(url);
        """)

        self.execute("""
        CREATE INDEX IF NOT EXISTS idx_links_source ON links(source_url);
        """)

        self.execute("""
        CREATE INDEX IF NOT EXISTS idx_links_target ON links(target_url);
        """)

        self.execute("""
        CREATE UNIQUE INDEX IF NOT EXISTS idx_content_hash ON pages(content_hash);
        """)