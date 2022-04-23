import pygame
from pygame.sprite import Sprite#sprite--小精灵

class Bullet(Sprite):#继承
    """管理飞船发射的子弹的类"""
    def __init__(self, ai_game) -> None:
        """在飞船当前位置创建一个子弹对象"""
        super().__init__()#调用父类构造,根据继承的类调用构造函数
        #给属性赋值
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.color=self.settings.bullet_color

        #在(0,0)处创建一个表示子弹的矩形,在设置到正确的位置
        self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midright=ai_game.ship.rect.midright#将子弹外界矩形的顶部设置到飞船外界矩形顶部的位置,实现子弹从飞船中间射出效果

        #存储用小数表示的子弹的位置,便于微调子弹速度
        self.x=float(self.rect.x)

    def update(self):
        """向上移动子弹"""
        self.x+=self.settings.bullet_speed#更新表示子弹位置的小数值
        self.rect.x=self.x#用更新后的小数值修改子弹外界矩形的坐标
    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)