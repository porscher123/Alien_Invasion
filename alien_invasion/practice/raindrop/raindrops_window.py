#导入模块
from os import remove
import sys
from time import sleep
from venv import create
from matplotlib.pyplot import flag
import pygame
from raindrop_settings import Settings
from raindrop import RainDrop

#创建游戏类
class raindrops_window:
    """管理游戏资源和行为的类"""
 
    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init() #c初始化背景设置
        self.settings = Settings()#创建设置对象,赋给游戏的设置属性
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#指定尺寸创建一个窗口,赋给游戏的screen属性
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("raindrops")#caption->说明文字

        #创建雨滴编组
        self.raindrops = pygame.sprite.Group()
        self._create_raindrops() #创建雨滴们

        
    def _check_events(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():#遍历事件列表
            if event.type == pygame.QUIT:#用户点击关闭按钮使,检测到QUIT事件
                sys.exit()#调用系统函数关闭窗口


#?雨滴相关
    def _create_raindrop(self, raindrop_numer, row_number):
        """创建一个雨滴,并放在当前行"""
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size #获取雨滴矩形的宽度和高度
        # 计算放置该雨滴的坐标
        raindrop.x = raindrop_width +  2 * raindrop_width * raindrop_numer # raindrop_number从0开始
        raindrop.y = -raindrop_height +  (2 * raindrop_height + 25) * row_number 
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop.y
        self.raindrops.add(raindrop) #加入到雨滴编队中

    def _create_raindrops(self):
        """创建雨滴群
           横向间距为雨滴宽度
           纵向间距是雨滴高度 
        """
        raindrop = RainDrop(self)# 创建一个雨滴,用来获取宽度
        raindrop_width, raindrop_height = raindrop.rect.size #获取雨滴矩形的宽度和高度

        # 计算每行可容纳多少雨滴
        available_space_x = self.settings.screen_width 
        number_raindrops_x = available_space_x //  (2 * raindrop_width)
        # 计算可容纳多少行
      
        available_space_y = (self.settings.screen_height )
        number_rows = available_space_y //  (2 * raindrop_height)
        
        for row_number in range(number_rows): #创建每行
            for raindrop_numer in range(number_raindrops_x): #创建该行的每列
                #创建一个雨滴并将其加入当前行
                self._create_raindrop(raindrop_numer,row_number)




    def _create_a_row(self): #在第一行创建一行雨滴
        raindrop = RainDrop(self)
        raindrop_width, raindrop_height = raindrop.rect.size 
        available_space_x = self.settings.screen_width - raindrop_width
        number_raindrops_x = available_space_x //  raindrop_width

        for column in range(number_raindrops_x): 
            self._create_raindrop(column,0) 




    def _check_raindrop_ends(self):
        flag=0
        for raindrop in self.raindrops.copy(): #超过屏幕边界的删除
            if raindrop.rect.bottom > self.screen_rect.bottom:
                self.raindrops.remove(raindrop)
                flag=1
        if flag:
            self._create_a_row()
              
        
    def _update_raindrops(self):
        self._check_raindrop_ends()
        self.raindrops.update()
        

    def _update_screen(self): 
        self.screen.fill((0,0,0))
        self.raindrops.draw(self.screen)
        pygame.display.update()


    def show(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = raindrops_window()#创建游戏实例
    ai.show()#运行游戏
