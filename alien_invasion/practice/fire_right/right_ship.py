import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game) -> None:
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen#飞船的屏幕属性与游戏界面一致
        self.settings = ai_game.settings#
        self.screen_rect = ai_game.screen.get_rect()#飞船的屏幕矩形和游戏场景的矩形一致

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("images\ship_right.bmp")#加载飞船图片
        self.rect = self.image.get_rect()#将图片的外界矩形,作为自己的矩形框

        #对于每艘新飞船,都将其放在左边中央
        self.rect.midleft = self.screen_rect.midleft

        print(self.rect)
        self.y = float(self.rect.y)

        #用于判断是否移动的标志
        self.moving_up = False #上移标志
        self.moving_down = False #下移标志


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        
    def update(self):
        """根据自己属性,更新飞船的位置"""
        if self.moving_up and self.rect.top > 0: #矩形顶部不超过屏幕上方
            self.y -= self.settings.ship_speed#修改浮点数self.x的大小

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom: #矩形底部低于屏幕下方
            self.y += self.settings.ship_speed
        #根据self.x更新rect.x,只取self.x的整数部分
        self.rect.y = self.y