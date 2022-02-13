from taso import Taso
from tason_lukija import Kartta
import pygame
import sys

pygame.init()

kello = pygame.time.Clock()

kartta = Kartta('./tasot/taso1.txt')
screen = pygame.display.set_mode((kartta.pituus, kartta.korkeus))
taso = Taso(kartta.data, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    taso.update()
    
    pygame.display.update()
    kello.tick(60)
