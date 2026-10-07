import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent / "database"
BASE_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = BASE_DIR / "products.db"



conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

def init_db():

    cursor.execute("PRAGMA foreign_keys = ON;")
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL,
        bar_code TEXT UNIQUE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS product_lots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        quant INTEGER DEFAULT 0,
        price REAL DEFAULT 0.0,
        date_valid TEXT NOT NULL,
        location TEXT DEFAULT 'LOJA',
        status TEXT DEFAULT 'NORMAL',
        FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
    );
    """)
    conn.commit() # Agora dentro da função!

init_db()