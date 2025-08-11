import sqlite3
from datetime import datetime

def adicionar_fase(nome, descricao, restricao, resposta_certa):
    con = sqlite3.connect("banco.db")
    cursor = con.cursor()

    cursor.execute("""
    INSERT INTO Fases(nome, descricao, restricao, resposta_certa)
    values(?, ?, ?, ?)
""", (nome, descricao, restricao, resposta_certa))
    
    con.commit()
    con.close()



def atualizar_fase(coluna_alvo, novo_valor, coluna_filtro, valor_filtro):
    con = sqlite3.connect("banco.db")
    cursor = con.cursor()
    
    query = f"""
        UPDATE Fases
        SET {coluna_alvo} = ?
        WHERE {coluna_filtro} = ?
    """
    cursor.execute(query, (novo_valor, valor_filtro))
    
    con.commit()
    con.close()

    
def remover_fase(nome):
    con = sqlite3.connect("banco.db")
    cursor = con.cursor()

    cursor.execute("""
    DELETE FROM Fases
    where nome = ?
""", (nome,))
    
    con.commit()
    con.close()


def listar_fases():
    con = sqlite3.connect("banco.db")
    cursor = con.cursor()
    cursor.execute("SELECT id, nome, descricao FROM Fases")
    fases = cursor.fetchall()
    con.close()
    return fases