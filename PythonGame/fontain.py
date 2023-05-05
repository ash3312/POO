import pygame
import time
import random

pygame.init()

screen_res = (500,500)

screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)

pygame.display.set_caption("Fontain")

screen.fill((0,0,0))
pygame.display.flip()


def gen_color():
    return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def create_rect(x, y):
    rect = pygame.Rect(x, y, random.randint(25,50), random.randint(10,50))

    return pygame.draw.rect(screen, gen_color(), rect, 0, 0)

def create_circle(x, y):
    return pygame.draw.circle(screen, gen_color(), (x,y), random.randint(25,50), 0)

def create_polygon(x, y):
    points = [(x,y), (x + 50 ,y ) ,(x ,y + 50)]
    return pygame.draw.polygon(screen, gen_color(), points, 0)

def choose(x, y):
   no = random.randint(1,3)
   match no:
        case 1:
            return create_rect(x, y)
        case 2:
            return create_circle(x, y)
        case 3:
            return create_polygon(x, y)

running = True
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

        if evt.type == pygame.MOUSEMOTION:
            time.sleep(0.01)
            screen.fill((0,0,0))
            mouse_pos = pygame.mouse.get_pos()
            choose(mouse_pos[0], mouse_pos[1])

            pygame.display.flip()