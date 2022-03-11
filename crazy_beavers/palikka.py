import pygame
from palikka_rekisteri import rekisteroi_palikka
from perus_palikka import Palikka
import pathlib

class Kivi(Palikka):
    symboli = 'K'
    
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.image.load('./kuvat/palikat/kivi.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (koko, koko))
        self.rect = self.image.get_rect(topleft=paikka)

    def osuma(self):
        pass
        
class Suo(Palikka):
    symboli = 'S'
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.surface.Surface((koko, koko))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=paikka)

class Ametysti(Palikka):
    symboli = 'A'

    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.image.load('./kuvat/palikat/amethyst.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (koko, koko))
        self.rect = self.image.get_rect(topleft=paikka)

    def osuma(self):
        pass
        
class Vesi(Palikka):
    symboli = 'V'
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.image.load('./kuvat/palikat/vesi.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (koko, koko))
        self.rect = self.image.get_rect(topleft=paikka)
    def osuma(self):
        print("ui majava ui!")
        
rekisteroi_palikka(Kivi)
rekisteroi_palikka(Suo)
rekisteroi_palikka(Vesi)
rekisteroi_palikka(Ametysti)