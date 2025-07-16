import pygame
from telas.base import Tela
from game.telas.fasevariaveis import Variaveis

class MenuFases(Tela):
    def __init__(self, titulo="Fases"):
        super().__init__(titulo)
        self.background = pygame.image.load('imagens/background2.png').convert()
        self.snake = pygame.image.load('imagens/snake.png').convert_alpha()
        self.snake = pygame.transform.scale(self.snake, (90, 60))
        self.titulo_fonte = pygame.font.Font(self.caminho_fonte, 35)

        self.botoes = [
            {"retangulo": pygame.Rect(390, 200, 550, 80), "cor": self.cor},
            {"retangulo": pygame.Rect(390, 290, 550, 80), "cor": self.cor},
            {"retangulo": pygame.Rect(390, 380, 550, 80), "cor": self.cor},
            {"retangulo": pygame.Rect(390, 470, 550, 80), "cor": self.cor},
        ]

    def atualizar(self, dt):
        pass

    def desenhar(self):
        fundo = pygame.transform.scale(self.background, self.screen.get_size())
        self.screen.blit(fundo, (0, 0))

        titulo = self.fonte_titulo.render(self.titulo, True, self.cor_titulo)
        self.screen.blit(titulo, (600, 80))
        
        self.screen.blit(self.snake, (525, 112))

        self.texto_botoes = ["Variáveis", "Condicionais", "Loops", "Funções"]
        fonte = pygame.font.Font("fontes/Ithaca.ttf", 28)

        for i, botao in enumerate(self.botoes):
            if botao["retangulo"].collidepoint(pygame.mouse.get_pos()):
                self.cor = self.cor_borda  # muda a cor se mouse estiver em cima
            else:
                self.cor = self.cor_botao

            pygame.draw.rect(self.screen, self.cor, botao["retangulo"], border_radius=15)
            pygame.draw.rect(self.screen, self.cor_borda, botao["retangulo"], 7, border_radius=15)

            texto = self.texto_botoes[i]
            texto_renderizado = fonte.render(texto, True, self.cor_titulo)
            texto_botao = texto_renderizado.get_rect(center=botao["retangulo"].center)
            self.screen.blit(texto_renderizado, texto_botao)

    def eventos(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            if self.botoes[0]["retangulo"].collidepoint(pos): 
                return Variaveis()