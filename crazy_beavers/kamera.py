import pygame
from abc import ABC, abstractmethod

vec = pygame.math.Vector2

class Kamera:
    def __init__(self, player):
        self.player = player
        self.offset = vec(0,0)
        self.offset_float = vec(0,0)
        self.DISPLAY_W, DISPLAY_H = 480, 270
        self.CONST = vec(0,0)
    def setmethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()



class KameraScroll(ABC):
    def __init__(self, kamera, player):
        self.kamera = kamera
        self.player = player

    #@abstractmethod
    def scroll(self):
        pass


class Seuraa(KameraScroll):
    def __init__(self, kamera, player):
        KameraScroll.__init__(self, kamera, player)
    def scroll(self):
        self.kamera.offset_float.x += (self.player.rect.x - self.kamera.offset_float.x + self.kamera.CONST.x)
        self.kamera.offset_float.y += (self.player.rect.y - self.kamera.offset_float.y + self.kamera.CONST.y)
        self.kamera.offset.x, self.kamera.offset.y = int(self.kamera.offset_float.x), int(self.kamera.offset_float.y)

class Raja(KameraScroll):
    class Seuraa(KameraScroll):
        def __init__(self, kamera, player):
            KameraScroll.__init__(self, kamera, player)

        def scroll(self):
            self.kamera.offset_float.x += (self.player.rect.x - self.kamera.offset_float.x + self.kamera.CONST.x)
            self.kamera.offset_float.y += (self.player.rect.y - self.kamera.offset_float.y + self.kamera.CONST.y)
            self.kamera.offset.x, self.kamera.offset.y = int(self.kamera.offset_float.x), int(self.kamera.offset_float.y)
            self.kamera.offset.x = max(self.player.left_border, self.kamera.offset.x)
            self.kamera.offset.x = min(self.kamera.offset.x, self.player.right_border - self.kamera.DISPLAY_W)

class Auto(KameraScroll):
    def __init__(self,kamera, player):
        KameraScroll.__init__(self,kamera, player)
    def scroll(self):
        self.kamera.offset.x += 1


