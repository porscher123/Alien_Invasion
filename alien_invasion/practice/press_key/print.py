import pygame
import sys

class Window:
    def __init__(self) -> None:
        pygame.init()
        self.screen=pygame.display.set_mode((800,600))
        self.screen_rect=self.screen.get_rect()
    
    def _check_keydown_events(self,event): 
        if event.type == pygame.KEYDOWN: # 如果是按下键事件
            print(event.key) #打印键值
    
    def _check_events(self):
        for event in pygame.event.get():
            self._check_keydown_events(event)
            if event.type == pygame.QUIT:
                sys.exit()
    def show_window(self):
        while True:
            self._check_events()
            self.screen.fill((233,233,233))
            pygame.display.update()

my_window=Window()
my_window.show_window()
