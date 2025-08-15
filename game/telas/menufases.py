import pygame
from telas.base import Tela
from fases.estruturafase import Fase
from fases.novafase import NovaFase
from database.crudfase import listar_fases

class MenuFases(Tela):
    def __init__(self, titulo="Fases"):
        super().__init__(titulo)
        self.background = pygame.image.load('imagens/background2.png').convert()
        self.snake = pygame.image.load('imagens/snake.png').convert_alpha()
        self.snake = pygame.transform.scale(self.snake, (90, 60))
        self.engrenagem = pygame.image.load('imagens/engrenagem.png')
        self.engrenagem = pygame.transform.scale(self.engrenagem, (60, 60))

        self.engrenagem_pos = (1260, 40)
        # posição e tamanho da engrenagem
        self.engrenagem_rect = pygame.Rect(self.engrenagem_pos, self.engrenagem.get_size())
        self.mostrar_popup = False
        self.opcoes_popup = ["Nova Fase", "Listar Fases", "Listar Alunos"]

        self.retangulos_popup = [
            pygame.Rect(self.engrenagem_pos[0] - 200, self.engrenagem_pos[1] + 15, 200, 40), 
            pygame.Rect(self.engrenagem_pos[0] - 200, self.engrenagem_pos[1] + 56, 200, 40),  
            pygame.Rect(self.engrenagem_pos[0] - 200, self.engrenagem_pos[1] + 98, 200, 40)  
        ]

        self.fases = listar_fases()  # busca do banco
        self.botoes = []
        for i, fase in enumerate(self.fases):
            rect = pygame.Rect(390, 200 + i * 90, 550, 80)
            self.botoes.append({"retangulo": rect, "cor": self.cor, "nome": fase[1]})  # fase[1] = nome da fase


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

            texto = botao["nome"]  # nome vindo do banco
            texto_renderizado = fonte.render(texto, True, self.cor_titulo)
            texto_botao = texto_renderizado.get_rect(center=botao["retangulo"].center)
            self.screen.blit(texto_renderizado, texto_botao)

        if self.mostrar_popup:
            for i, rect in enumerate(self.retangulos_popup):
                pygame.draw.rect(self.screen, (200, 200, 200), rect, border_radius=8)  # fundo branco
                pygame.draw.rect(self.screen, (20, 20, 20), rect, 4, border_radius=8)

                texto_popup = self.opcoes_popup[i]
                texto_popup_renderizado = pygame.font.Font("fontes/Ithaca.ttf", 19).render(texto_popup, True, (0, 0, 0))
                texto_rect = texto_popup_renderizado.get_rect(center=rect.center)
                self.screen.blit(texto_popup_renderizado, texto_rect)

        self.screen.blit(self.engrenagem, (1250, 40))

    def eventos(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos

            for i, botao in enumerate(self.botoes):
                if botao["retangulo"].collidepoint(pos):
                    fase_nome = botao['nome']
                    return Fase(fase_nome)

            if self.engrenagem_rect.collidepoint(pos):
                self.mostrar_popup = not self.mostrar_popup
                return None  # Só abrir/fechar o popup

            if self.mostrar_popup:
                for i, rect in enumerate(self.retangulos_popup):
                    if rect.collidepoint(pos):
                        if i == 0:  # primeira opção "Nova Fase"
                            print("Clicou em Nova Fase!")  # pra debug
                            return NovaFase()