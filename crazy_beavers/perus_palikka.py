import pygame

PALIKAN_KOKO = 64

class Palikka(pygame.sprite.Sprite):
    """Kantaluokka kaikille paikallaan oleville palikoille (katso palikka.py)
    
    """
    def __init__(self, paikka, koko):
        super().__init__()
        self.symboli = None
        self.image = None
        self.rect = None