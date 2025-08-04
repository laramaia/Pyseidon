import sqlite3
from datetime import datetime

def adicionar_fase(nome, descricao, restricao, resposta_certa):
    con = sqlite3.connect("db.py")
    cursor = sqlite3.Cursor()

    cursor.execute("""
    INSERT INTO Fases(nome, descricao, restricao, resposta_certa)
    values(?, ?, ?, ?)
""", (nome, descricao, restricao, resposta_certa))
    
    con.commit()
    con.close()