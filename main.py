import pygame

pygame.init()

BLACK = (0,0,0)
RED = (255,0,0)
PURPLE = (138,0,196)
WHITE = (255,255,255)

WIDTH = 800
HEIGHT = 600

CENTER = (WIDTH // 2, HEIGHT // 2 - 150)
RADIUS = 7

BALL_POS = (WIDTH // 2, HEIGHT // 2 + 100)
BALL_RAD = 15

LINE_S = (WIDTH // 2 - 1, HEIGHT // 2 - 150)
LINE_E = (WIDTH // 2 - 1, HEIGHT // 2 + 100)
THICKNESS = 2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pendulum")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)

    pygame.draw.line(screen, WHITE, LINE_S, LINE_E, THICKNESS)
    pygame.draw.circle(screen, RED, CENTER, RADIUS)
    pygame.draw.circle(screen, PURPLE, BALL_POS, BALL_RAD)

    pygame.display.flip()

pygame.quit()   