from telas.base import Tela
import pygame

class Variaveis(Tela):
    def __init__(self, titulo="Desafios de Variáveis"):
        super().__init__(titulo)

        self.background2 = pygame.image.load('imagens/background2.png').convert()
        self.fonte = pygame.font.Font('fontes/Pixeled.ttf', 35)
        self.desafios = [
            {"nome": "Declarando variáveis", "coordenadas": pygame.Rect(390, 150, 550, 80)},
            {"nome": "Desafio 2", "coordenadas": pygame.Rect(390, 240, 550, 80)},
        ]

    def desenhar(self):
        fundo = pygame.transform.scale(self.background2, self.screen.get_size())
        self.screen.blit(fundo, (0, 0))

        for desafio in self.desafios:
            pygame.draw.rect(self.screen, self.cor, desafio["coordenadas"], border_radius=15)
            pygame.draw.rect(self.screen, self.cor_borda, desafio["coordenadas"], 7, border_radius=15)

    def atualizar(self, dt):
        pass