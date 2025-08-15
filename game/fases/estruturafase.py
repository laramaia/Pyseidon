from database.crudfase import buscar_fase_por_nome
from telas.base import Tela
import time
import pygame

class Fase(Tela):
    def __init__(self, nome_fase, titulo="Fases"):
        super().__init__(titulo)
        self.background = pygame.image.load('imagens/background2.png').convert()
        self.detalhes_fase = pygame.Rect(80, 40, 580, 600)
        self.editor_codigo = pygame.Rect(700, 40, 580, 520)
        self.fonte = pygame.font.Font("fontes/Ithaca.ttf", 26)
        self.botao_voltar = {"rect": pygame.Rect(740, 580, 200, 60), "cor": (255, 255, 255), "texto": "Voltar"}
        self.botao_submeter = {"rect": pygame.Rect(1020, 580, 200, 60), "cor": (255, 255, 255), "texto": "Subemeter"}

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

        pygame.draw.rect(self.screen, (255, 179, 71), self.detalhes_fase)
        pygame.draw.rect(self.screen, (0, 0, 0), self.editor_codigo)

        pygame.draw.rect(self.screen, self.botao_voltar["cor"], self.botao_voltar["rect"])
        pygame.draw.rect(self.screen, (0, 0, 0), self.botao_voltar["rect"], 1)
        texto_botao = self.fonte.render(self.botao_voltar["texto"], True, (0, 0, 0))
        texto_retangulo = texto_botao.get_rect(center=self.botao_voltar["rect"].center)
        self.screen.blit(texto_botao, texto_retangulo)

        pygame.draw.rect(self.screen, self.botao_submeter["cor"], self.botao_submeter["rect"])
        pygame.draw.rect(self.screen, (0, 0, 0), self.botao_submeter["rect"], 1)
        texto_botao = self.fonte.render(self.botao_submeter["texto"], True, (0, 0, 0))
        texto_retangulo = texto_botao.get_rect(center=self.botao_submeter["rect"].center)
        self.screen.blit(texto_botao, texto_retangulo)

        descricao_titulo = self.fonte.render("Descrição:", True, (0, 0, 0))
        self.screen.blit(descricao_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 20))

        descricao_texto = self.fonte.render(self.descricao, True, (0, 0, 0))
        self.screen.blit(descricao_texto, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 60))

        restricao_titulo = self.fonte.render("Restrição:", True, (0, 0, 0))
        self.screen.blit(restricao_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 120))

        restricao_texto = self.fonte.render(self.restricao, True, (0, 0, 0))
        self.screen.blit(restricao_texto, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 160))


    def eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_voltar["rect"].collidepoint(event.pos):
                from telas.menufases import MenuFases
                time.sleep(0.5)
                return MenuFases()
            
    def atualizar(self, dt):
        pass