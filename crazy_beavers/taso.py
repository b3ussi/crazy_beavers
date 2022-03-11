from tausta import Tausta
from palikka import Palikka
from pelaaja import Majava
from palikka_rekisteri import hae_palikka
from perus_palikka import PALIKAN_KOKO
from tason_lukija import lue_taso
import pygame


class Taso:
    def __init__(self, taso_data, surface, bg_obj):
        self.taso_data = taso_data
        
        self.pituus = len(self.taso_data[0]) * PALIKAN_KOKO
        self.korkeus = len(self.taso_data) * PALIKAN_KOKO
        self.tausta_shift = 0
        self.surface = surface
        self.palikat = pygame.sprite.Group()
        self.pelaaja = pygame.sprite.GroupSingle()
        #self.tausta_olio = Tausta("./kuvat/taustat/bg1.png", 1920, 1080)
        #self.tausta = pygame.sprite.GroupSingle()
        #self.tausta.add(self.tausta_olio)
        self.tausta = bg_obj
        self.surface.blit(self.tausta, (0, 0))
        self.valmistele()
        self.tausta_poikkeama = 0
        

    def vaakatormayksen_tarkistus(self):
        pelaaja = self.pelaaja.sprite
        pelaaja.rect.x += pelaaja.liike.x

        for palikka in self.palikat.sprites():
            if palikka.rect.colliderect(pelaaja.rect):
                if pelaaja.liike.x < 0:
                    pelaaja.rect.left = palikka.rect.right
                elif pelaaja.liike.x > 0:
                    pelaaja.rect.right = palikka.rect.left

    def pystytormayksen_tarkistus(self):
        pelaaja = self.pelaaja.sprite
        pelaaja.painovoimaa()

        for palikka in self.palikat.sprites():
            if palikka.rect.colliderect(pelaaja.rect):
                palikka.osuma()
                if pelaaja.liike.y < 0:
                    pelaaja.rect.bottom = palikka.rect.top
                elif pelaaja.liike.y > 0:
                    pelaaja.rect.top = palikka.rect.bottom
                pelaaja.liike.y = 0

        #print(f"lopullinen {pelaaja.suunta}")

    def valmistele(self):
        # looppaa koko se data missä kivet jne on
        for rivi_numero, rivi in enumerate(self.taso_data):
            for sarake_numero, symboli in enumerate(rivi):
                if not symboli.isspace():
                    palikka_luokka = hae_palikka(symboli)
                    palikka = palikka_luokka((sarake_numero * PALIKAN_KOKO, rivi_numero * PALIKAN_KOKO), PALIKAN_KOKO)

                    if isinstance(palikka, Majava):
                        self.pelaaja.add(palikka)
                    else:
                        self.palikat.add(palikka)
                    # print(f"lisätty {type(palikka)}")

    def testaa_tormaykset(self):
        pass


    def update(self):
        self.scroll_x()
        self.surface.blit(self.tausta, (self.tausta_poikkeama, 0))
        self.palikat.update(self.tausta_shift)
        # self.tausta.update(self.tausta_shift)
        self.palikat.draw(self.surface)
        self.pelaaja.draw(self.surface)
        #self.tausta.draw(self.surface)
        self.vaakatormayksen_tarkistus()
        self.pystytormayksen_tarkistus()
        self.pelaaja.update()
        print(self.tausta_shift)
        
        
    def scroll_x(self):
        pelaaja = self.pelaaja.sprite
        paikka_x = pelaaja.rect.centerx
        suunta = pelaaja.suunta
        
        if paikka_x > 400 and suunta > 0:
            self.tausta_shift = -1
            pelaaja.rect.centerx = 400
        elif paikka_x < 200 and suunta < 0:
            self.tausta_shift = 1
        else:
            self.tausta_shift = 0
        
        self.tausta_poikkeama += self.tausta_shift
        
        #self.surface.blit()
            
            
            
        
