import pygame

PALIKAN_KOKO = 32

class Palikka(pygame.sprite.Sprite):
    """Kantaluokka kaikille paikallaan oleville palikoille (katso palikka.py)
    """

    def __init__(self, paikka, koko):
        super().__init__()
        self.symboli = None
        self.image = None
        self.rect = None

    def osuma(self):
        pass