import pygame
import time

pygame.init()


screen_res = (400,500)

screen = pygame.display.set_mode(screen_res, pygame.RESIZABLE)

pygame.display.set_caption("moving")

screen.fill((100,100,100))
pygame.display.flip()

rect = pygame.Rect(0,0,50,50)
pygame.draw.rect(screen, "blue", rect, 2, 0)
pygame.display.flip()

# new_rect = rect.move(50,50)
# pygame.draw.rect(screen, "blue", new_rect, 2, 0)
# pygame.display.flip()

running = True
while running:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            running = False

        if evt.type == pygame.MOUSEMOTION:
            time.sleep(0.01)
            screen.fill((100,100,100))
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            #rect.move_ip(mouse_pos[0],mouse_pos[1])
            rect = pygame.Rect(mouse_pos[0],mouse_pos[1],50,50)
            new_rect = rect.inflate(150, 150)
            pygame.draw.rect(screen, "blue", new_rect, 2, 0)
            pygame.display.flip()