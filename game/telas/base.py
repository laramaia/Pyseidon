import pygame

class Tela:
    def __init__(self, titulo=""):
        self.screen = pygame.display.set_mode((1380,700))
        self.titulo = titulo
        self.caminho_fonte = "fontes/Pixeled.ttf"
        self.fonte_titulo = pygame.font.Font(self.caminho_fonte, 40)
        self.cor_titulo = (247, 248, 250)
        self.cor_botao = (38, 71, 153)
        self.cor_borda = (40, 55, 135)
        self.cor = self.cor_botao # inicializa cor dos botões

    def desenhar(self): # visual (background, textos, etc.) da tela
        if self.titulo:
            texto = self.fonte_titulo.render(self.titulo, True, self.cor_titulo)
            self.screen.blit(texto, (50, 30))  # posição ajustável

    def eventos(self, event): # troca de telas
        pass

        def extrair_frames(self, spritesheet, columns, rows):
            frames = []
            for row in range(rows):
                for col in range(columns):
                    rect = pygame.Rect(col * self.frame_width, row * self.frame_height, self.frame_width, self.frame_height)
                    frame = spritesheet.subsurface(rect).copy()
                    frames.append(frame)
            return frames
