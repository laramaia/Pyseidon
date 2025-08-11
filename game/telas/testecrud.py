from game.database.crudfase import adicionar_fase, remover_fase, listar_fases
import game.database.db

menu = input("Escolha:\n\n[1] Adicionar fase\n[2] Remover fase\n[3] Listar fases\n\n")

if menu == "1":
    nome = input("Nome da fase: ")
    descricao = input("Descrição: ")
    restricao = input("Restrição: ")
    resposta = input("Resposta correta: ")

    adicionar_fase(nome, descricao, restricao, resposta)
    print("Fase salva no banco com sucesso!")

if menu =="2":
    nome = input("Nome da fase: ")

    remover_fase(nome)
    print(f"Fase {nome} removida.")

else:
    print(listar_fases())