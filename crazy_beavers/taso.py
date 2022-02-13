from palikka import Palikka
from palikka_rekisteri import hae_palikka
from perus_palikka import PALIKAN_KOKO
from tason_lukija import lue_taso
import pygame


class Taso:
    def __init__(self, taso_data, surface):
        self.taso_data = taso_data
        
        self.pituus = len(self.taso_data[0]) * PALIKAN_KOKO
        self.korkeus = len(self.taso_data) * PALIKAN_KOKO
        
        self.surface = surface
        self.palikat = pygame.sprite.Group()
        self.valmistele()
    
    def valmistele(self):
        # looppaa koko se data missä kivet jne on
        for rivi_numero, rivi in enumerate(self.taso_data):
            for sarake_numero, symboli in enumerate(rivi):
                if not symboli.isspace():
                    palikka_luokka = hae_palikka(symboli)
                    palikka = palikka_luokka((sarake_numero * PALIKAN_KOKO, rivi_numero * PALIKAN_KOKO), PALIKAN_KOKO)
                    self.palikat.add(palikka)
                    # print(f"lisätty {type(palikka)}")

    def update(self):
        self.palikat.draw(self.surface)
        