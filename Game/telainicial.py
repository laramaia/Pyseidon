import pygame
import sys
 
pygame.init()

screen = pygame.display.set_mode((1200, 680))
clock = pygame.time.Clock()

pygame.font.init() 
fonte = pygame.font.Font('fontes/Pixeled.ttf', 40)

frame_width = 640
frame_height = 540
frame_duration = 270  # milissegundos por frame

logo = pygame.image.load("Imagens/logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (450, 220))

def extrair_frames(spritesheet, columns, rows):
    frames = []
    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height)
            frame = spritesheet.subsurface(rect).copy()
            frames.append(frame)
    return frames

# Carrega as spritesheets
sheet1 = pygame.image.load("Imagens/background1.1.png").convert()
sheet2 = pygame.image.load("Imagens/background1.2.png").convert()

# Extrai os frames das duas imagens
frames1 = extrair_frames(sheet1, columns=3, rows=2)
frames2 = extrair_frames(sheet2, columns=3, rows=2)

# Junta todos os frames
all_frames = frames1 + frames2
total_frames = len(all_frames)

# Controle de animação
frame_index = 0
tempo_frame = 0

running = True
while running:
    dt = clock.tick(60)
    tempo_frame += dt

    if tempo_frame >= frame_duration:
        tempo_frame = 0
        frame_index = (frame_index + 1) % total_frames

    # Redimensiona o frame
    frame_redimensionado = pygame.transform.scale(all_frames[frame_index], screen.get_size())
    screen.blit(frame_redimensionado, (0, 0))

    # Ajusta a logo
    x = (screen.get_width() - logo.get_width()) // 2
    y = (screen.get_height() - logo.get_height()) // 2
    screen.blit(logo, (x, y))

        # Título
    titulo = "PYSEIDON"
    cor_texto = (247, 248, 250)
    renderizacao_texto = fonte.render(titulo, True, cor_texto)
    screen.blit(renderizacao_texto, (464, 420))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()