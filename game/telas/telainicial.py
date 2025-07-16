from telas.base import Tela
from telas.menufases import MenuFases
import pygame

class TelaInicial(Tela):
    def __init__(self, titulo="PYSEIDON"):
        super().__init__(titulo)
        self.fundo = pygame.image.load("imagens/background1.1.png").convert()
        self.logo = pygame.image.load("imagens/logo.png").convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (450, 220))
        self.texto = "CLIQUE PARA COMEÇAR"

        self.frame_width = 640
        self.frame_height = 540
        self.frame_duration = 270
        self.frame_index = 0
        self.tempo_frame = 0

        sheet1 = pygame.image.load("imagens/background1.1.png").convert()
        sheet2 = pygame.image.load("imagens/background1.2.png").convert()
        self.frames = self.extrair_frames(sheet1, 3, 2) + self.extrair_frames(sheet2, 3, 2)

    def extrair_frames(self, spritesheet, columns, rows):
        frames = []
        for row in range(rows):
            for col in range(columns):
                rect = pygame.Rect(col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height)
                frame = spritesheet.subsurface(rect).copy()
                frames.append(frame)
        return frames
    
    def atualizar(self, dt):
        # dt = tempo passado desde o último update (milissegundos)
        self.tempo_frame += dt
        if self.tempo_frame >= self.frame_duration:
            self.tempo_frame = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)

    def desenhar(self):
        frame_atual = pygame.transform.scale(self.frames[self.frame_index], self.screen.get_size())
        self.screen.blit(frame_atual, (0, 0))

        titulo = self.fonte_titulo.render(self.titulo, True, self.cor_titulo)
        self.screen.blit(titulo, (540, 420))

        fonte_menor = pygame.font.SysFont("Arial", 15)
        texto_renderizado = fonte_menor.render(self.texto, True, (240, 240, 240))
        self.screen.blit(texto_renderizado, (620, 520))

        x = (self.screen.get_width() - self.logo.get_width()) // 2
        y = (self.screen.get_height() - self.logo.get_height()) // 2
        self.screen.blit(self.logo, (x, y))

    def eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False
            return MenuFases()