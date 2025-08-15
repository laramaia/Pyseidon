from telas.base import Tela
from database.crudfase import adicionar_fase
import pygame

class NovaFase(Tela):
    def __init__(self, titulo="Nova Fase"):
        super().__init__(titulo)

        self.background = pygame.image.load("imagens/background1.1.png").convert()
        self.fonte_titulo = pygame.font.Font(self.caminho_fonte, 26)
        self.fonte = pygame.font.Font("fontes/Ithaca.ttf", 26)
        self.botao_salvar = {"rect": pygame.Rect(570, 520, 200, 50), "cor": (100, 200, 100), "texto": "Salvar"}

        self.frame_width = 640
        self.frame_height = 540
        self.frame_duration = 270
        self.frame_index = 0
        self.tempo_frame = 0

        sheet1 = pygame.image.load("imagens/background1.1.png").convert()
        sheet2 = pygame.image.load("imagens/background1.2.png").convert()
        self.frames = self.extrair_frames(sheet1, 3, 2) + self.extrair_frames(sheet2, 3, 2)

        self.retangulos_formulario = [
            {"label": "nome", "coordenadas": pygame.Rect(400, 190, 550, 50)},
            {"label": "descricao", "coordenadas": pygame.Rect(400, 270, 550, 50)},
            {"label": "restricao", "coordenadas": pygame.Rect(400, 350, 550, 50)},
            {"label": "resposta_certa", "coordenadas": pygame.Rect(400, 430, 550, 50)},
        ]

        self.valores_formulario = ["", "", "", ""]
        self.indice_campo = 0

    def desenhar(self):
        frame_atual = pygame.transform.scale(self.frames[self.frame_index], self.screen.get_size())
        self.screen.blit(frame_atual, (0, 0))

        titulo = self.fonte_titulo.render(self.titulo, True, (37, 27, 92))
        self.screen.blit(titulo, (580, 70))

        for i, campo in enumerate(self.retangulos_formulario):
            pygame.draw.rect(self.screen, (243, 243, 243), campo["coordenadas"])
            pygame.draw.rect(self.screen, (0, 0, 0), campo["coordenadas"], 4)

            descricao_label = self.fonte.render(campo["label"], True, self.cor_titulo)  
            self.screen.blit(descricao_label, (campo["coordenadas"].x + 5, campo["coordenadas"].y - 25))

            texto_digitado = self.valores_formulario[i]
            texto_renderizado = self.fonte.render(texto_digitado, True, (0, 0, 0))
            self.screen.blit(texto_renderizado, (campo["coordenadas"].x + 10, campo["coordenadas"].y + 15))

        # botao
        pygame.draw.rect(self.screen, self.botao_salvar["cor"], self.botao_salvar["rect"])
        pygame.draw.rect(self.screen, (0, 0, 0), self.botao_salvar["rect"], 2)

        texto_botao = self.fonte.render(self.botao_salvar["texto"], True, (0, 0, 0))
        texto_retangulo = texto_botao.get_rect(center=self.botao_salvar["rect"].center)
        self.screen.blit(texto_botao, texto_retangulo)

    def atualizar(self, dt):
        # dt = tempo passado desde o último update (milissegundos)
        self.tempo_frame += dt
        if self.tempo_frame >= self.frame_duration:
            self.tempo_frame = 0
            self.frame_index = (self.frame_index + 1) % len(self.frames)

    def eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i, campo in enumerate(self.retangulos_formulario):
                if campo["coordenadas"].collidepoint(event.pos):
                    self.indice_campo = i

            if self.botao_salvar["rect"].collidepoint(event.pos):
                self.salvar_fase()

        elif event.type == pygame.KEYDOWN:
            # Tecla Enter salva a fase
            if event.key == pygame.K_RETURN:
                self.salvar_fase()

            # Tecla é adicionada ao campo de texto
            else:
                self.valores_formulario[self.indice_campo] += event.unicode

    def salvar_fase(self):
        nome, descricao, restricao, resposta_certa = self.valores_formulario

        if nome != "" and descricao != "" and restricao != "" and resposta_certa != "":
            adicionar_fase(nome, descricao, restricao, resposta_certa)
            print("Fase adicionada com sucesso!")
            self.valores_formulario = ["", "", "", ""]  # limpa os campos após salvar
        else:
            print("Preencha todos os campos antes de salvar.")