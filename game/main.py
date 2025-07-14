import pygame
from telas.telainicial import TelaInicial

pygame.init() 
pygame.font.init()  
clock = pygame.time.Clock()
tela = TelaInicial()

running = True
while running:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Captura o retorno da tela atual para trocar de tela se necessário
        proxima_tela = tela.eventos(event)
        if proxima_tela:
            tela = proxima_tela

    tela.atualizar(dt)  # atualiza animação e lógica com o delta time
    tela.desenhar()

    pygame.display.flip()

pygame.quit()
