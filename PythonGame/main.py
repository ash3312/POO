import pygame

pygame.init()

res = (500, 300)
screen = pygame.display.set_mode(res, pygame.RESIZABLE)

pygame.display.set_caption("First window")

screen.fill((55, 90, 255))

pygame.display.flip()

# line
# screen , color, point1, point2
pygame.draw.line(screen, "red", (0, 0), (500, 300))
pygame.draw.aaline(screen, "red", (0, 0), (500, 300))  # anti alias

# point
# screen , color, point, point
pygame.draw.line(screen, "green", (10, 10), (10, 10))

# rect
# rect x1 y1 x2 y2
# screen , color, rect, width, radius
rect = pygame.Rect(50, 50, 100, 150)
pygame.draw.rect(screen, "pink", rect, 10, 15)

# circle
# screen , color, center, rayon, width
pygame.draw.circle(screen, "magenta", (200, 100), 50, 10)

# polygon
# screen , color, points, width
points = [(10, 10), (150, 10), (100, 100)]
pygame.draw.polygon(screen, "white", points, 5)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.WINDOWRESIZED:
            screen.fill((55, 90, 255))
            pygame.display.flip()
