import sqlite3
from pathlib import Path

DB_FILE = Path('allcare_leads.db')

def get_connection():
    """Initiates connection with the database file in the root directory"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    #core leads table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS leads(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        place_id TEXT UNIQUE,
        business_name TEXT NOT NULL,
        phone TEXT,
        website TEXT,
        address TEXT,
        pincode TEXT,
        source TEXT
        lead_score INTEGER DEFAULT 0,
        intent_summary TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
        """
        )
    
    #Creates regional pincodes table
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS regional_pincodes(
        pincode TEXT PRIMARY KEY,
        area TEXT NOT NULL,
        city TEXT NOT NULL,
        state TEXT NOT NULL)
        """
    )

    conn.commit()
    conn.close()

    print("DATABASE initialized succesfully!")
    
if __name__ == "__main__":
    init_db()