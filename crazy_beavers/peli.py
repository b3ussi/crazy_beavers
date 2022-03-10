from taso import Taso
from tason_lukija import Kartta
from kamera import*
import pygame
import sys
from pelaaja import*







pygame.init()

kello = pygame.time.Clock()
kartta = Kartta('./tasot/taso1.txt')
screen = pygame.display.set_mode((400,300), pygame.RESIZABLE)
taso = Taso(kartta.data, screen)
bg = pygame.image.load("./kuvat/taustat/bg1.png").convert()

# majava = Majava(12,12)
# player = majava
# kamera = Kamera(majava)
# follow = Seuraa(kamera, majava)
# border = Raja(kamera, majava)
# auto = Auto(kamera, majava)
# kamera.setmethod(Seuraa)


while True:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # nappaimet = pygame.key.get_pressed()
    # if nappaimet[pygame.K_w]:
    #    print("W laulaa")

    screen.blit(bg, (0, 0))

    taso.update()

    pygame.display.update()
    kello.tick(60)
