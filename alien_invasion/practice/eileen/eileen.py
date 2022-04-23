import pygame
from settings import Settings
class Eileen:
    def __init__(self,window) -> None:

        self.screen = window.screen #设置爱凌的矩形在主屏幕上
        self.screen_rect = window.screen.get_rect()
        self.image = pygame.image.load("images\\250.png")# 加载爱凌图片
        self.rect = self.image.get_rect()# 获取爱凌矩形
        self.rect.center = self.screen_rect.center #初始放置爱凌到屏幕中央
        self.settings = Settings()

        #向四个方向移动的状态
        self.moving_up = False
        self.moving_down = False
        self.movin_left = False
        self.moving_right = False

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def update_position(self): #更新爱凌位置
        # 比较爱凌矩形的四个边的位置与窗口的矩形的四个边框位置关系
        if self.moving_up and self.rect.top > self.screen_rect.top: #向上移动,爱凌上边框小于窗口上边框
            self.rect.y -= self.settings.eileen_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom: #向下移动,爱凌下边框大于窗口下边框
            self.rect.y += self.settings.eileen_speed
        elif self.movin_left and self.rect.left > self.screen_rect.left: #向左移动,爱凌左边框大于窗口左边框
            self.rect.x -= self.settings.eileen_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right: #向有移动,爱凌右边框小于窗口右边框
            self.rect.x += self.settings.eileen_speed