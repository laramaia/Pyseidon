import requests
from fases.feedbackfase import TelaSucesso, TelaFracasso
from database.crudfase import buscar_fase_por_nome
from telas.base import Tela
import time
import pygame

# source_code = input("Digite o código Python a ser executado: ")
class Fase(Tela):
    def __init__(self, nome_fase, titulo="Fases"):
        super().__init__(titulo)
        self.background = pygame.image.load('imagens/background2.png').convert()
        self.detalhes_fase = pygame.Rect(80, 40, 580, 600)
        self.editor_codigo = pygame.Rect(700, 40, 580, 520)
        self.fonte = pygame.font.Font("fontes/Ithaca.ttf", 26)
        self.botao_voltar = {"rect": pygame.Rect(740, 580, 200, 60), "cor": (232, 73, 68), "texto": "Voltar"}
        self.botao_submeter = {"rect": pygame.Rect(1020, 580, 200, 60), "cor": (40, 55, 135), "texto": "Submeter"}
        self.resultado_execucao = ""

        self.codigo = "" 
        self.cursor_pos = len(self.codigo)  # Posição do cursor no texto

        fase = buscar_fase_por_nome(nome_fase)
        if fase:
            self.nome, self.descricao, self.restricao, self.resposta_certa = fase
        else:
            self.nome = nome_fase
            self.descricao = ""
            self.restricao = ""
            self.resposta_certa = ""

    def desenhar(self):
        fundo = pygame.transform.scale(self.background, self.screen.get_size())
        self.screen.blit(fundo, (0, 0))

        pygame.draw.rect(self.screen, (221, 170, 75), self.detalhes_fase)
        pygame.draw.rect(self.screen, (58, 55, 55), self.editor_codigo)

        pygame.draw.rect(self.screen, self.botao_voltar["cor"], self.botao_voltar["rect"])
        pygame.draw.rect(self.screen, (0, 0, 0), self.botao_voltar["rect"], 1)
        texto_botao = self.fonte.render(self.botao_voltar["texto"], True, (255, 255, 255))
        texto_retangulo = texto_botao.get_rect(center=self.botao_voltar["rect"].center)
        self.screen.blit(texto_botao, texto_retangulo)

        pygame.draw.rect(self.screen, self.botao_submeter["cor"], self.botao_submeter["rect"])
        pygame.draw.rect(self.screen, (0, 0, 0), self.botao_submeter["rect"], 1)
        texto_botao = self.fonte.render(self.botao_submeter["texto"], True, (255, 255, 255))
        texto_retangulo = texto_botao.get_rect(center=self.botao_submeter["rect"].center)
        self.screen.blit(texto_botao, texto_retangulo)

        desafio_titulo = self.fonte.render("DESAFIO:", True, (0, 0, 0))
        self.screen.blit(desafio_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 20))

        desafio_texto = self.fonte.render(self.nome, True, (0, 0, 0))
        self.screen.blit(desafio_texto, (self.detalhes_fase.x + 100, self.detalhes_fase.y + 20))

        descricao_titulo = self.fonte.render("DESCRIÇÃO", True, (0, 0, 0))
        self.screen.blit(descricao_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 70))

        descricao_texto = self.fonte.render(self.descricao, True, (0, 0, 0))
        self.screen.blit(descricao_texto, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 100))

        restricao_titulo = self.fonte.render("RESTRIÇÃO", True, (0, 0, 0))
        self.screen.blit(restricao_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 160))

        restricao_texto = self.fonte.render(self.restricao, True, (0, 0, 0))
        self.screen.blit(restricao_texto, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 190))

        texto_codigo = self.fonte.render(self.codigo, True, (255, 255, 255))
        self.screen.blit(texto_codigo, (self.editor_codigo.x + 20, self.editor_codigo.y + 20))

        resposta_titulo = self.fonte.render("RESPOSTA", True, (0, 0, 0))
        self.screen.blit(resposta_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 220))

        resposta_texto = self.fonte.render(self.resposta_certa, True, (0, 0, 0))
        self.screen.blit(resposta_texto, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 250))


        linhas = self.codigo.split('\n')
        y = self.editor_codigo.y + 20
        for linha in linhas:
            texto_codigo = self.fonte.render(linha, True, (255, 255, 255))
            self.screen.blit(texto_codigo, (self.editor_codigo.x + 20, y))
            y += texto_codigo.get_height() + 5

        # desenhar resultado da execução abaixo do editor
        resultado_titulo = self.fonte.render("Resultado: ", True, (255, 255, 255))
        self.screen.blit(resultado_titulo, (self.editor_codigo.x + 20, y + 10))

        resultado_linhas = self.resultado_execucao.split('\n')
        y += resultado_titulo.get_height() + 20
        for linha in resultado_linhas:
            texto_resultado = self.fonte.render(linha, True, (200, 200, 200))
            self.screen.blit(texto_resultado, (self.editor_codigo.x + 20, y))
            y += texto_resultado.get_height() + 2

    def eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_voltar["rect"].collidepoint(event.pos):
                from telas.menufases import MenuFases
                time.sleep(0.5)
                return MenuFases()
            
            if self.botao_submeter["rect"].collidepoint(event.pos):
                self.resultado_execucao = self.executar_codigo(self.codigo)

                if self.resposta_certa.strip() == self.resultado_execucao.strip():
                    return TelaSucesso()
                else:
                    return TelaFracasso()

            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  # Apagar o último caractere
                self.codigo = self.codigo[:-1]
            elif event.key == pygame.K_RETURN:  # Finaliza o código
                pass
            else:
                self.codigo += event.unicode
            
    def atualizar(self, dt):
        pass


    def executar_codigo(self, codigo, versao="3.10.0"):
        url = "https://emkc.org/api/v2/piston/execute"

        payload = {
            "language": "python",
            "version": versao,
            "files": [
                {
                    "content": codigo
                }
            ]
        }

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            resultado = response.json()
            return resultado.get("run", {}).get("stdout", "") 
        else:
            return f"Erro na execução: {response.text}"
