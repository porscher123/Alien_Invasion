import pygame 
from pygame.sprite import Sprite

class Star(Sprite):
    """一个星星的类"""
    def __init__(self,ai_game) -> None:
        super().__init__()
        self.screen = ai_game.screen
        self.image = pygame.image.load("images\\star2.png")
        self.rect = self.image.get_rect()

        self.rect.x = float(self.rect.width)
        self.rect.y = float(self.rect.height)

        

    