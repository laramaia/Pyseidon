import pygame
from telas.base import Tela

class TelaSucesso(Tela):
    def __init__(self, titulo="Você passou!"):
        super().__init__(titulo)

        self.background = pygame.image.load("imagens/background1.1.png").convert()
        self.fonte_titulo = pygame.font.Font("fontes/Ithaca.ttf", 42)
        self.caixa = pygame.Rect(440, 160, 500, 400)

        self.frame_width = 640
        self.frame_height = 540
        self.frame_duration = 270
        self.frame_index = 0
        self.tempo_frame = 0

        sheet1 = pygame.image.load("imagens/background1.1.png").convert()
        sheet2 = pygame.image.load("imagens/background1.2.png").convert()
        self.frames = self.extrair_frames(sheet1, 3, 2) + self.extrair_frames(sheet2, 3, 2)

    def desenhar(self):
        frame_atual = pygame.transform.scale(self.frames[self.frame_index], self.screen.get_size())
        self.screen.blit(frame_atual, (0, 0))

        pygame.draw.rect(self.screen, self.cor, self.caixa)
        pygame.draw.rect(self.screen, self.cor_borda, self.caixa, 7)

        titulo = self.fonte_titulo.render(self.titulo, True, self.cor_titulo)
        self.screen.blit(titulo, (610, 190))

    def atualizar(self, dt):
        self.tempo_frame += dt
        if self.tempo_frame >= self.frame_duration:
            self.tempo_frame = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)


class TelaFracasso(Tela):
    def __init__(self, titulo="Tente novamente"):
        super().__init__(titulo)

        self.background = pygame.image.load("imagens/background1.1.png").convert()
        self.fonte_titulo = pygame.font.Font("fontes/Ithaca.ttf", 42)
        self.caixa = pygame.Rect(440, 160, 500, 400)

        self.frame_width = 640
        self.frame_height = 540
        self.frame_duration = 270
        self.frame_index = 0
        self.tempo_frame = 0

        sheet1 = pygame.image.load("imagens/background1.1.png").convert()
        sheet2 = pygame.image.load("imagens/background1.2.png").convert()
        self.frames = self.extrair_frames(sheet1, 3, 2) + self.extrair_frames(sheet2, 3, 2)

    def desenhar(self):
        frame_atual = pygame.transform.scale(self.frames[self.frame_index], self.screen.get_size())
        self.screen.blit(frame_atual, (0, 0))

        pygame.draw.rect(self.screen, self.cor, self.caixa)
        pygame.draw.rect(self.screen, self.cor_borda, self.caixa, 7)

        titulo = self.fonte_titulo.render(self.titulo, True, self.cor_titulo)
        self.screen.blit(titulo, (610, 190))

    def atualizar(self, dt):
        self.tempo_frame += dt
        if self.tempo_frame >= self.frame_duration:
            self.tempo_frame = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)