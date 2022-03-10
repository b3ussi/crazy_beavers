from perus_palikka import Palikka
from palikka_rekisteri import rekisteroi_palikka
import pygame

class Majava(Palikka):
    symboli = 'M'
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.image.load('./kuvat/hahmot/majava.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (koko, koko))
        self.rect = self.image.get_rect(topleft=paikka)
        self.liike = pygame.math.Vector2(0, 0)
        self.painovoima = 1.0
        self.hyppy_nopeus = 9

    def lue_nappaimet(self):
        nappaimet = pygame.key.get_pressed()
        if nappaimet[pygame.K_a]:
            self.liike.x = -1
        elif nappaimet[pygame.K_d]:
            self.liike.x = 1
        else:
            self.liike.x = 0

        if nappaimet[pygame.K_SPACE]:
            self.hyppy()

    def painovoimaa(self):
        self.liike.y -= self.painovoima
        self.rect.y -= self.liike.y

    def hyppy(self):
        self.liike.y = self.hyppy_nopeus * 1

    def update(self):
        self.lue_nappaimet()
        self.rect.x += self.liike.x
        #self.painovoimaa()





rekisteroi_palikka(Majava)