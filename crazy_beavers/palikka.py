import pygame
from palikka_rekisteri import rekisteroi_palikka
from perus_palikka import Palikka
import pathlib

class Kivi(Palikka):
    symboli = 'K'
    
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.image.load('./kuvat/palikat/kivi.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = paikka)

        
class Suo(Palikka):
    symboli = 'S'
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.surface.Surface((koko, koko))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft = paikka)

        
class Vesi(Palikka):
    symboli = 'V'
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        self.image = pygame.image.load('./kuvat/palikat/vesi.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = paikka)

        
rekisteroi_palikka(Kivi)
rekisteroi_palikka(Suo)
rekisteroi_palikka(Vesi)