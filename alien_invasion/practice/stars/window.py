import pygame
import sys 
from pygame.sprite import Sprite
from star import Star
from stars_settings import Settings
from random import randint

class Window:
    def __init__(self) -> None:
        pygame.init() #初始化窗口设置
        self.screen = pygame.display.set_mode((900,780)) #设置大小,返回一个surface
        self.screen_rect = self.screen.get_rect() #获得surface的rect
        pygame.display.set_caption("Stars")#设置标题
        self.stars = pygame.sprite.Group()#设置星星编组属性
        self.settings = Settings()
        self._create_stars()#调用函数创建星星编组
        


    def _check_events(self): #检测退出事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


    def _create_start(self,row,column):
        """创建一个星星"""
        star = Star(self)
        start_x = self.settings.interval
        start_y = self.settings.interval
        star_width, star_height = star.rect.size
        star.rect.x = start_x + (2 * star_width) * column
        star.rect.y = start_y + (2 * star_height) * row
        self.stars.add(star)



    def _create_stars(self):
        """创建一群星星"""
        star = Star(self)
        star_width, star_height = star.rect.size
         
        #
        available_space_x = self.screen_rect.width - (2 * self.settings.interval)
        number_column = available_space_x // (2 * star_width)
        #
        available_space_y = self.screen_rect.height - (2 * self.settings.interval)
        number_row = available_space_y // (2 * star_height)
        # for row in range(number_row):
        #     for column in range(number_column):
        stars_num = 20
        for num in range(stars_num):
            row = randint(0,number_row) #随机选择一行
            column = randint(0,number_column) #随机选择一列
            print(row,column)
            self._create_start(row,column) #在此行此列创建星星
        
    def update_screen(self):
        self._check_events()
        self.screen.fill((0,0,0))
        self.stars.draw(self.screen)
        pygame.display.update()

    def show(self):
        while True:
            self.update_screen()

window = Window()
window.show()