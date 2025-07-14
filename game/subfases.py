import pygame

def executar_subfases():
    pygame.init()

    screen = pygame.display.set_mode((1380, 700))
    clock = pygame.time.Clock()

    pygame.font.init() 
    fonte = pygame.font.Font('fontes/Pixeled.ttf', 35)

    background2 = pygame.image.load('Imagens/background2.png').convert()

    running = True
    while running:
        frame_redimensionado = pygame.transform.scale(background2, screen.get_size())
        screen.blit(frame_redimensionado, (0, 0))

        titulo = "Desafios"
        cor_texto = (247, 248, 250)
        renderizacao_texto = fonte.render(titulo, True, cor_texto)
        screen.blit(renderizacao_texto, (540, 100))

        retangulo1 = pygame.draw.rect(screen, (38, 71, 153), (320, 200, 550, 80), border_radius=15)
        borda1 = pygame.draw.rect(screen, (40, 55, 135), (320, 200, 550, 80), 7, border_radius=15)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    pygame.quit()

executar_subfases()