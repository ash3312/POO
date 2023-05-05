import pygame
import time

pygame.init()
surface_res = (500, 500)
surface = pygame.display.set_mode(surface_res, pygame.RESIZABLE)
i = 0
black_color = (0, 0, 0)
red_color = (255, 0, 0)
blue_color = (0, 0 , 255)
monRectangle = pygame.Rect(200, 200, 30, 30)
monMur = pygame.Rect(200, 200, 30, 30)
pygame.draw.rect(surface, red_color, monRectangle)
pygame.display.flip()

collision = False
running = True
while running: # main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    time.sleep(0.01)
    surface.fill(black_color)
    if(monRectangle.colliderect(monMur)):
        collision = True
    if (collision == True):
        monRectangle.move_ip(-1, 0)
        collision = False
    else:
        monRectangle.move_ip(1, 0)
    pygame.draw.rect(surface, red_color, monRectangle)
    pygame.draw.rect(surface, blue_color, monMur)
    pygame.display.flip()
