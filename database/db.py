import sqlite3

con = sqlite3.connect("db.py")
cursor = sqlite3.Cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Fases (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        descricao TEXT, 
        restricao TEXT,
        resposta_certa TEXT
    )
""")