import pygame
from pygame.sprite import Sprite
from settings import Settings
class Alien(Sprite):
    """表示一个外星人的类"""
    def __init__(self,ai_game) -> None:
        """初始化外星人并设置其其实位置"""
        super().__init__()#调用父类构造
        self.screen = ai_game.screen#添加到游戏主屏幕中

        self.settings = ai_game.settings #!外星人的设置与游戏类的设置一致,否则在游戏类中修改设置不会影响外星人
        # 加载外星人图像,并设置其rect属性
        self.image = pygame.image.load("alien_invasion\\images\\alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕的左上角附近
        # rect.x,rect.y表示外界矩形的其实坐标
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置
        # 更关心外星人的水平速度
        self.x = float(self.rect.x)


    def check_edges(self):
        """如果外星人位于屏幕边缘,返回true"""
        screen_rect =self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update(self):
        """向右移动外星人"""
        self.x += (self.settings.alien_speed *
                    self.settings.fleet_direction) #*向右时,x增加,向左时,x减少
        self.rect.x = self.x #*self.x 可以记录保存小数,以追准外星人准确的位置,使得可加上浮点速度
