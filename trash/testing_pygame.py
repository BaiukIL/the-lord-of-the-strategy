import pygame
import time


pygame.init()
screen = pygame.display.set_mode((1920, 800))

surf = pygame.Surface((500, 300))
surf.fill(pygame.Color('white'))

pygame.draw.rect(surf, pygame.Color('red'), pygame.Rect(surf.get_rect().x // 2, surf.get_rect().y // 2, surf.get_rect().width // 2, surf.get_rect().height // 2))
bord_size = 3
pygame.draw.rect(surf, pygame.Color('blue'), surf.get_rect(), bord_size)
r = pygame.Rect(bord_size // 2, bord_size // 2, surf.get_rect().width - bord_size, surf.get_rect().height - bord_size)
subsurf = surf.subsurface(r)

screen.blit(surf, (0, 100))
pygame.display.flip()
time.sleep(2)
screen.fill(pygame.Color('black'))
screen.blit(subsurf, (0 + bord_size // 2, 100 + bord_size // 2))
pygame.display.flip()
input()
