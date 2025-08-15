from telas.base import Tela
import pygame

class Fase(Tela):
    def __init__(self, titulo="Fases"):
        super().__init__(titulo)
        self.background = pygame.image.load('imagens/background2.png').convert()
        self.detalhes_fase = pygame.Rect(80, 40, 580, 600)
        self.editor_codigo = pygame.Rect(700, 40, 580, 600)

    def desenhar(self):
        fundo = pygame.transform.scale(self.background, self.screen.get_size())
        self.screen.blit(fundo, (0, 0))

        pygame.draw.rect(self.screen, (255, 179, 71), self.detalhes_fase)
        pygame.draw.rect(self.screen, (0, 0, 0), self.editor_codigo)

    def atualizar(self, dt):
        pass