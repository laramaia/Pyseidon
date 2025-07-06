import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 680))
clock = pygame.time.Clock()

pygame.font.init() 
fonte = pygame.font.Font('fontes/Pixeled.ttf', 35)

background2 = pygame.image.load('Imagens/background2.png').convert()
snake = pygame.image.load('Imagens/snake.png').convert_alpha()
snake = pygame.transform.scale(snake, (90, 50))

running = True
while running:
    frame_redimensionado = pygame.transform.scale(background2, screen.get_size())
    screen.blit(frame_redimensionado, (0, 0))

    titulo = "Fases"
    cor_texto = (247, 248, 250)
    renderizacao_texto = fonte.render(titulo, True, cor_texto)
    screen.blit(renderizacao_texto, (540, 100))
    screen.blit(snake, (462, 129))

    retangulo1 = pygame.draw.rect(screen, (38, 71, 153), (320, 200, 550, 80), border_radius=15)
    borda1 = pygame.draw.rect(screen, (40, 55, 135), (320, 200, 550, 80), 7, border_radius=15)

    retangulo2 = pygame.draw.rect(screen, (38, 71, 153), (320, 290, 550, 80), border_radius=15)
    borda2 = pygame.draw.rect(screen, (40, 55, 135), (320, 290, 550, 80), 7, border_radius=15)

    retangulo3 = pygame.draw.rect(screen, (38, 71, 153), (320, 380, 550, 80), border_radius=15)
    borda3 = pygame.draw.rect(screen, (40, 55, 135), (320, 380, 550, 80), 7, border_radius=15)

    retangulo4 = pygame.draw.rect(screen, (38, 71, 153), (320, 470, 550, 80), border_radius=15)
    borda4 = pygame.draw.rect(screen, (40, 55, 135), (320, 470, 550, 80), 7, border_radius=15)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()