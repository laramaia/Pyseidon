import sqlite3

con = sqlite3.connect("banco.db")
cursor = con.cursor()

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

con.commit()
con.close()