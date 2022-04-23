import pygame
from pygame.sprite import Sprite
from raindrop_settings import Settings
class RainDrop(Sprite):
    """表示一个雨滴的类"""
    def __init__(self,raindrops_window) -> None:
        """初始化雨滴并设置其其实位置"""
        super().__init__()#调用父类构造
        self.screen = raindrops_window.screen#添加到游戏主屏幕中
        self.screen_rect  =self.screen.get_rect()
        self.settings = raindrops_window.settings
        # 加载雨滴图像,并设置其rect属性
        self.image = pygame.image.load("images\\raindrop2.png")
        self.rect = self.image.get_rect()

        # rect.x,rect.y表示外界矩形的其实坐标
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.y = float(self.rect.y) #精确雨滴的垂直位置
    def update(self):
        self.y += self.settings.rain_speed #向下移动雨滴
        self.rect.y = self.y 
