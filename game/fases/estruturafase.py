from database.crudfase import buscar_fase_por_nome
from RestrictedPython import compile_restricted
from RestrictedPython import safe_globals
from RestrictedPython import limited_builtins
from RestrictedPython import utility_builtins
from telas.base import Tela
import time
import pygame

# source_code = input("Digite o código Python a ser executado: ")
class Fase(Tela):
    def __init__(self, nome_fase, titulo="Fases"):
        super().__init__(titulo)
        self.background = pygame.image.load('imagens/background2.png').convert()
        self.detalhes_fase = pygame.Rect(80, 40, 580, 600)
        self.editor_codigo = pygame.Rect(700, 40, 580, 520)
        self.fonte = pygame.font.Font("fontes/Ithaca.ttf", 26)
        self.botao_voltar = {"rect": pygame.Rect(740, 580, 200, 60), "cor": (232, 73, 68), "texto": "Voltar"}
        self.botao_submeter = {"rect": pygame.Rect(1020, 580, 200, 60), "cor": (40, 55, 135), "texto": "Submeter"}

        self.codigo = "" 
        self.cursor_pos = len(self.codigo)  # Posição do cursor no texto

        fase = buscar_fase_por_nome(nome_fase)
        if fase:
            self.nome, self.descricao, self.restricao, self.resposta_certa = fase
        else:
            self.nome = nome_fase
            self.descricao = ""
            self.restricao = ""
            self.resposta_certa = ""

    def desenhar(self):
        fundo = pygame.transform.scale(self.background, self.screen.get_size())
        self.screen.blit(fundo, (0, 0))

        pygame.draw.rect(self.screen, (221, 170, 75), self.detalhes_fase)
        pygame.draw.rect(self.screen, (58, 55, 55), self.editor_codigo)

        pygame.draw.rect(self.screen, self.botao_voltar["cor"], self.botao_voltar["rect"])
        pygame.draw.rect(self.screen, (0, 0, 0), self.botao_voltar["rect"], 1)
        texto_botao = self.fonte.render(self.botao_voltar["texto"], True, (255, 255, 255))
        texto_retangulo = texto_botao.get_rect(center=self.botao_voltar["rect"].center)
        self.screen.blit(texto_botao, texto_retangulo)

        pygame.draw.rect(self.screen, self.botao_submeter["cor"], self.botao_submeter["rect"])
        pygame.draw.rect(self.screen, (0, 0, 0), self.botao_submeter["rect"], 1)
        texto_botao = self.fonte.render(self.botao_submeter["texto"], True, (255, 255, 255))
        texto_retangulo = texto_botao.get_rect(center=self.botao_submeter["rect"].center)
        self.screen.blit(texto_botao, texto_retangulo)

        desafio_titulo = self.fonte.render("DESAFIO:", True, (0, 0, 0))
        self.screen.blit(desafio_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 20))

        desafio_texto = self.fonte.render(self.nome, True, (0, 0, 0))
        self.screen.blit(desafio_texto, (self.detalhes_fase.x + 100, self.detalhes_fase.y + 20))

        descricao_titulo = self.fonte.render("DESCRIÇÃO", True, (0, 0, 0))
        self.screen.blit(descricao_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 70))

        descricao_texto = self.fonte.render(self.descricao, True, (0, 0, 0))
        self.screen.blit(descricao_texto, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 100))

        restricao_titulo = self.fonte.render("RESTRIÇÃO", True, (0, 0, 0))
        self.screen.blit(restricao_titulo, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 160))

        restricao_texto = self.fonte.render(self.restricao, True, (0, 0, 0))
        self.screen.blit(restricao_texto, (self.detalhes_fase.x + 20, self.detalhes_fase.y + 190))

        texto_codigo = self.fonte.render(self.codigo, True, (255, 255, 255))
        self.screen.blit(texto_codigo, (self.editor_codigo.x + 20, self.editor_codigo.y + 20))

    def eventos(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.botao_voltar["rect"].collidepoint(event.pos):
                from telas.menufases import MenuFases
                time.sleep(0.5)
                return MenuFases()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:  # Apagar o último caractere
                self.codigo = self.codigo[:-1]
            elif event.key == pygame.K_RETURN:  # Finaliza o código
                pass
            else:
                self.codigo += event.unicode
            
    def atualizar(self, dt):
        pass

    def executar_codigo(self, codigo):
        try:
            byte_code = compile_restricted(codigo, '<string>', 'exec')

            safe_locals = {}
            safe_globals.update({
                '__builtins__': {
                    'print': print, 
                    'range': range,
                    'list': list,
                    'tuple': tuple,
                    'str': str,
                    'int': int,
                    'float': float,
                },
            })

            exec(byte_code, safe_globals, safe_locals)

        except Exception as e:
            print(f"Erro ao executar código: {e}")
