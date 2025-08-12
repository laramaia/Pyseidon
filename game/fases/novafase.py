from telas.base import Tela
import pygame

class NovaFase(Tela):
    def __init__(self, titulo="Nova Fase"):
        super().__init__(titulo)

        self.background = pygame.image.load("imagens/background1.1.png").convert()
        self.fonte = pygame.font.Font("fontes/Ithaca.ttf", 20)

        self.frame_width = 640
        self.frame_height = 540
        self.frame_duration = 270
        self.frame_index = 0
        self.tempo_frame = 0

        sheet1 = pygame.image.load("imagens/background1.1.png").convert()
        sheet2 = pygame.image.load("imagens/background1.2.png").convert()
        self.frames = self.extrair_frames(sheet1, 3, 2) + self.extrair_frames(sheet2, 3, 2)

        self.retangulos_formulario = [
            {"label": "nome", "coordenadas": pygame.Rect(400, 160, 550, 50)},
            {"label": "descricao", "coordenadas": pygame.Rect(400, 240, 550, 50)},
            {"label": "restricao", "coordenadas": pygame.Rect(400, 320, 550, 50)},
            {"label": "resposta_certa", "coordenadas": pygame.Rect(400, 400, 550, 50)},
        ]

    def desenhar(self):
        frame_atual = pygame.transform.scale(self.frames[self.frame_index], self.screen.get_size())
        self.screen.blit(frame_atual, (0, 0))

        titulo = self.fonte_titulo.render(self.titulo, True, self.cor_titulo)
        self.screen.blit(titulo, (490, 50))

        i = 140
        for campo in self.retangulos_formulario:
            pygame.draw.rect(self.screen, (243, 243, 243), campo["coordenadas"])
            pygame.draw.rect(self.screen, (0, 0, 0), campo["coordenadas"], 4)

            texto = self.fonte.render(campo["label"], True, (0, 0, 0))  
            self.screen.blit(texto, (410, i))

            i += 80

    def atualizar(self, dt):
        # dt = tempo passado desde o último update (milissegundos)
        self.tempo_frame += dt
        if self.tempo_frame >= self.frame_duration:
            self.tempo_frame = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)
