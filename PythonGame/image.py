import pygame
import time

pygame.init()
surface_res = (500, 500)
surface = pygame.display.set_mode(surface_res, pygame.RESIZABLE)
surface.fill((255,255,255))
pygame.display.flip()


image = pygame.image.load("img/logo.png").convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    surface.blit(image, [0,0])
    pygame.display.flip()
