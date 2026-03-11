from src.storage.database import Database

class Repository:

    def __init__(self):
        self.db = Database()
        self.db.initialize_schema()
    
    def save_page(self, url, title, status_code, html):
        self.db.execute("""
        INSERT OR IGNORE INTO PAGES (url, title, status_code, html)
        VALUES (?, ?, ?, ?)
        """, (url, title, status_code, html))
    
    def save_links(self, source_url, links):
        rows = [(source_url, link) for link in links]

        self.db.executemany("""
        INSERT INTO links (source_url, target_url)
        VALUES (?, ?)
        """, rows)
    
    def add_frontier(self, url, depth, priority=0):
        self.db.execute("""
        INSERT OR IGNORE INTO frontier (url, depth, priority)
        VALUES (?, ?, ?)
        """, (url, depth, priority))
    
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