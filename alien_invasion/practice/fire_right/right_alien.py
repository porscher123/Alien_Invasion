import pygame
from pygame.sprite import Sprite
from right_settings import Settings
class Alien(Sprite):
    def __init__(self,ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen

        self.settings = ai_game.settings 
        self.image = pygame.image.load("images\\alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y)
        self.direction = 1 #* 保存这个外星人的方向

    def check_edges(self): #* 边界检测
        screen_rect =self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= screen_rect.top:
            return True

    def update(self): #* 上下移动外星人
        self.y += (self.settings.alien_speed * self.direction) 
        self.rect.y = self.y 
