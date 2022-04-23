import pygame

class Ship:
    """管理飞船的类"""
    def __init__(self,ai_game) -> None:
        """初始化飞船并设置其初始位置"""
        self.screen = ai_game.screen#飞船的屏幕属性与游戏界面一致
        self.settings = ai_game.settings#
        self.screen_rect = ai_game.screen.get_rect()#飞船的屏幕矩形和游戏场景的矩形一致

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load("E:\\PythonFiles\项目\\alien_invasion\\images\\ship.bmp")#加载飞船图片
        self.rect = self.image.get_rect()#将图片的外界矩形,作为自己的矩形框

        #对于每艘新飞船,都将其放在底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        print(self.rect)
        self.x = float(self.rect.x)

        #用于判断是否移动的标志
        self.moving_right = False
        self.moving_left = False


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕底端居中"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    def update(self):
        """根据自己属性,更新飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed#修改浮点数self.x的大小
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #根据self.x更新rect.x,只取self.x的整数部分
        self.rect.x = self.x