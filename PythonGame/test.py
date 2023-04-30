import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((400, 300), pygame.RESIZABLE)

pygame.display.set_caption("test window")

clock = pygame.time.Clock()


pygame.draw.line(screen, (255,255,255), (10,10),(100,100), 5 )

pygame.draw.line(screen, "white", (25,50),(25,50), 10)


r = pygame.Rect(15,20,60,80)
print(r.left)
print(r.top)
print(r.width)
print(r.height)
print(r.center, r.centerx, r.centery)
print(r.topleft, r.topright)
print(r.bottomleft, r.bottomright)
print(r.midleft, r.midright)

#r.center = (200,200)

pygame.draw.rect(screen, "green", r, 5, 5)



pygame.draw.circle(screen, "red", (45,145), 35, 5)


points = [(60,75), (80, 95), (125, 30)]
pygame.draw.polygon(screen, "blue", points, 5)


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(60)