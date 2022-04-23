from eileen import Eileen
from settings import Settings
import pygame
import sys

class Window:
    def __init__(self) -> None:
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        self.elien=Eileen(self)
    

    def _check_keydown_events(self,event):
        """检测上下左右键"""
        if event.key == pygame.K_UP:
            self.elien.moving_up=True
        elif event.key == pygame.K_DOWN:
            self.elien.moving_down=True
        elif event.key == pygame.K_LEFT:
            self.elien.movin_left=True
        elif event.key == pygame.K_RIGHT:
            self.elien.moving_right=True
        

    def _check_keyup_events(self,event):
        """检测上下左右键"""
        if event.key == pygame.K_UP:
            self.elien.moving_up=False
        elif event.key == pygame.K_DOWN:
            self.elien.moving_down=False
        elif event.key == pygame.K_LEFT:
            self.elien.movin_left=False
        elif event.key == pygame.K_RIGHT:
            self.elien.moving_right=False


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def show(self):
        while True:
            self.screen.fill(self.settings.bg_color)
            self._check_events()
            self.elien.blitme()
            self.elien.update_position()
            pygame.display.update()

window=Window()
window.show()