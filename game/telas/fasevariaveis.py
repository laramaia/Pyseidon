from telas.base import Tela
import pygame

class Variaveis(Tela):
    def __init__(self, titulo="Variaveis"):
        super().__init__(titulo)
        self.background2 = pygame.image.load('imagens/background2.png').convert()
        self.fonte = pygame.font.Font("fontes/Ithaca.ttf", 28)
        self.desafios = [
            {"nome": "Declarando variaveis", "coordenadas": pygame.Rect(390, 150, 550, 80)},
            {"nome": "Desafio 2", "coordenadas": pygame.Rect(390, 240, 550, 80)},
        ]

    def desenhar(self):
        fundo = pygame.transform.scale(self.background2, self.screen.get_size())
        self.screen.blit(fundo, (0, 0))

        titulo = self.fonte_titulo.render(self.titulo, True, self.cor_titulo)
        self.screen.blit(titulo, (520, 50))

        for desafio in self.desafios:
            pygame.draw.rect(self.screen, self.cor, desafio["coordenadas"], border_radius=15)
            pygame.draw.rect(self.screen, self.cor_borda, desafio["coordenadas"], 7, border_radius=15)

            texto = self.fonte.render(desafio["nome"], True, self.cor_titulo)  # Cor do texto (branco)
            texto_botao = texto.get_rect(center=desafio["coordenadas"].center)  # Centraliza o texto no botão
            self.screen.blit(texto, texto_botao)

    def atualizar(self, dt):
        pass