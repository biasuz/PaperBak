import sqlite3

DB_PATH = "paperbak.db"

def create_database():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript("""
        PRAGMA journal_mode = WAL;
        PRAGMA foreign_keys = ON;

        CREATE TABLE IF NOT EXISTS documents (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            title       TEXT NOT NULL,
            description TEXT,
            created_at  TEXT NOT NULL DEFAULT (datetime('now')),
            updated_at  TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE TABLE IF NOT EXISTS pages (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
            page_number INTEGER NOT NULL,
            content     BLOB,
            checksum    TEXT,
            created_at  TEXT NOT NULL DEFAULT (datetime('now')),
            UNIQUE (document_id, page_number)
        );

        CREATE TABLE IF NOT EXISTS backups (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            document_id INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
            file_path   TEXT NOT NULL,
            format      TEXT NOT NULL DEFAULT 'pdf',
            size_bytes  INTEGER,
            created_at  TEXT NOT NULL DEFAULT (datetime('now'))
        );

        CREATE INDEX IF NOT EXISTS idx_pages_document_id ON pages(document_id);
        CREATE INDEX IF NOT EXISTS idx_backups_document_id ON backups(document_id);
    """)

    conn.commit()
    conn.close()
    print(f"Database created: {DB_PATH}")

if __name__ == "__main__":
    create_database()
