from src.storage.database import Database

class Repository:

    def __init__(self):
        self.db = Database()
        self.db.initialize_schema()
    
    def save_page(self, url, title, status_code, html, hash_value):
        self.db.execute("""
        INSERT OR IGNORE INTO pages (url, title, status_code, html, content_hash)
        VALUES (?, ?, ?, ?, ?)
        """, (url, title, status_code, html, hash_value))

    def save_links(self, source_url, links):
        rows = [(source_url, link) for link in links]

        self.db.executemany("""
        INSERT OR IGNORE INTO links (source_url, target_url)
        VALUES (?, ?)
        """, rows)
    
    def add_frontier(self, url, depth, priority=0):
        self.db.execute("""
        INSERT OR IGNORE INTO frontier (url, depth, priority)
        VALUES (?, ?, ?)
        """, (url, depth, priority))
    
    def page_exists(self, content_hash):
        cursor = self.db.execute("""
        SELECT 1 FROM pages 
        WHERE content_hash = ? 
        LIMIT 1
        """, (content_hash,))

        return cursor.fetchone() is not None

    # ORDER BY priority DESC
    def get_next_frontier(self):
        cursor = self.db.execute("""
        SELECT url, depth, priority
        FROM frontier
        ORDER BY depth ASC
        LIMIT 1
        """)

        row = cursor.fetchone()

        if not row:
            return None
        
        self.db.execute(
            "DELETE FROM frontier WHERE url = ?",
            (row["url"],)
        )

        return row