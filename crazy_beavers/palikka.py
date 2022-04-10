import pygame
from palikka_rekisteri import rekisteroi_palikka
from perus_palikka import Palikka
import pathlib

class Kivi(Palikka):
    symboli = 'K'
    kuva = None
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        if not Kivi.kuva:
            Kivi.kuva = pygame.image.load('./kuvat/palikat/kivi.png').convert_alpha()
            Kivi.kuva = pygame.transform.scale(Kivi.kuva, (koko, koko))
        self.image = Kivi.kuva
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
    kuva = None
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        if not Ametysti.kuva:
            Ametysti.kuva = pygame.image.load('./kuvat/palikat/ametysti.png').convert_alpha()
            Ametysti.kuva = pygame.transform.scale(Ametysti.kuva, (koko, koko))
        self.image = Ametysti.kuva
        self.rect = self.image.get_rect(topleft=paikka)

    def osuma(self):
        pass


class AmetystiValipala(Palikka):
    symboli = '2'
    kuva = None
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        if not AmetystiValipala.kuva:
            AmetystiValipala.kuva = pygame.image.load('./kuvat/palikat/amethyst_valipala.png').convert_alpha()
            AmetystiValipala.kuva = pygame.transform.scale(AmetystiValipala.kuva, (koko, koko))
        self.image = AmetystiValipala.kuva
        self.rect = self.image.get_rect(topleft=paikka)

    def osuma(self):
        pass



class AmetystiLaskevaMaa(Palikka):
    symboli = '3'
    kuva = None
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        if not AmetystiLaskevaMaa.kuva:
            AmetystiLaskevaMaa.kuva = pygame.image.load('./kuvat/palikat/laskeva_maa.png').convert_alpha()
            AmetystiLaskevaMaa.kuva = pygame.transform.scale(AmetystiLaskevaMaa.kuva, (koko, koko))
        self.image = AmetystiLaskevaMaa.kuva

        self.rect = self.image.get_rect(topleft=paikka)

    def osuma(self):
        pass


class Kokoliilametisti(Palikka):
    symboli = '4'
    kuva = None
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        if not Kokoliilametisti.kuva:
            Kokoliilametisti.kuva = pygame.image.load('./kuvat/palikat/kokoliila_ametisti.png').convert_alpha()
            Kokoliilametisti.kuva = pygame.transform.scale(Kokoliilametisti.kuva, (koko, koko))
        self.image = Kokoliilametisti.kuva
        self.rect = self.image.get_rect(topleft=paikka)

    def osuma(self):
        pass


class Vesi(Palikka):
    symboli = 'V'
    kuva = None
    def __init__(self, paikka, koko):
        super().__init__(paikka, koko)
        if not Vesi.kuva:
            Vesi.kuva = pygame.image.load('./kuvat/palikat/vesi.png').convert_alpha()
            Vesi.kuva = pygame.transform.scale(Vesi.kuva, (koko, koko))
        self.image = Vesi.kuva
        self.rect = self.image.get_rect(topleft=paikka)
    def osuma(self):
        print("ui majava ui!")
        
rekisteroi_palikka(Kivi)
rekisteroi_palikka(Suo)
rekisteroi_palikka(Vesi)
rekisteroi_palikka(Ametysti)
rekisteroi_palikka(AmetystiValipala)
rekisteroi_palikka(AmetystiLaskevaMaa)
rekisteroi_palikka(Kokoliilametisti)