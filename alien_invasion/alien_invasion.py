#导入模块
import sys
from time import sleep
from turtle import Screen
from game_stats import GameStats
import pygame

from bullet import Bullet
from settings import Settings
from ship import Ship
from alien import Alien
from button import Button

#创建游戏类
class AlienInvasion:
    """管理游戏资源和行为的类"""
 
    def __init__(self) -> None: #构造函数
        """初始化游戏并创建游戏资源"""

        pygame.init() #初始化背景设置
        self.settings = Settings()#创建设置对象,赋给游戏的设置属性
        self.stats = GameStats(self) #创建一个用来存储游戏统计信息的实例
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#指定尺寸创建一个窗口,赋给游戏的screen属性

        pygame.display.set_caption("Alien Invasion")#caption->说明文字
        self.ship=Ship(self)#创建飞船(传入self),赋给属性ship

        #创建存储子弹的编组
        self.bullets = pygame.sprite.Group()
        #创建外星人编组
        self.aliens = pygame.sprite.Group()

        self._create_fleet() #创建外星人舰队

        self.play_button = Button(self, "Play")

        

#?事件相关
    def _check_keydown_events(self,event):
        # 检查按下事件
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:#按下空格键
            self._fire_bullet()
        elif event.key == pygame.K_q:#按Q键
            sys.exit()#退出程序
    
    def _check_keyup_events(self,event):
        # 检查释放事件
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right=False
        
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left=False
    

    def _check_play_button(self, mouse_pos):
        # 在玩家单击play按钮时开始新游戏
        # 检查鼠标点击位置是否在按钮的rect内
        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_events(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():    # 遍历事件列表
            if event.type == pygame.QUIT:   # 用户点击关闭按钮使,检测到QUIT事件
                sys.exit()  # 调用系统函数关闭窗口
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   # 检测按下方向键
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event) # 检测释放方向键
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  # 获取鼠标点击位置
                self._check_play_button(mouse_pos)  # 检测鼠标点击位置和按钮的位置关系
            


#?子弹相关
    def _fire_bullet(self): #创建一个子弹
        """创建一颗子弹,并将其加入编组"""
        if len(self.bullets) < self.settings.bullets_allowed:#判断当前编组内子弹数量是否在允许范围内
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_alien_collision(self): #响应子弹击中外星人
        """响应子弹荷外星人碰撞"""
        #删除发生碰撞的子弹和外星人
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,False,True
        )
        if not self.aliens: #如果外星人为空
            self.bullets.empty() #清空子弹
            self._create_fleet() #生成新的外星人群

    def _update_bullets(self): #检测子弹状态,更新子弹位置,删除消失子弹
        """更新子弹位置,并删除消失子弹"""
        self.bullets.update() #更新子弹组的位置,对编组操作,即对组内每个成员操作
        #删除消失的子弹
        for bullet in self.bullets.copy(): #遍历编组的副本
            if bullet.rect.bottom < 0: #如果矩形的底部的x小于0
                self.bullets.remove(bullet) #把该子弹在原编组中移除
        #检查子弹与外星人碰撞
        self._check_bullet_alien_collision()




#?外星人相关
    def _create_alien(self, alien_numer, row_number): #在某行某列创建一个外星人
        """创建一个外星人,并放在当前行"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size #获取外星人矩形的宽度和高度
        # 计算放置该外星人的坐标
        alien.x = alien_width + 2 * alien_width * alien_numer # alien_number从0开始
        alien.y = alien_height + 2 * alien_height * row_number 
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien) #加入到外星人编队中

    def _create_fleet(self): #创建外星人编队
        """创建外星人群
           横向间距为外星人宽度
           纵向间距是外星人高度 
        """
        alien = Alien(self)# 创建一个外星人,用来获取宽度
        alien_width, alien_height = alien.rect.size #获取外星人矩形的宽度和高度

        # 计算每行可容纳多少外星人
        available_space_x = self.settings.screen_width - (2 * alien_width)#计算横向可用空间
        number_aliens_x = available_space_x // (2 * alien_width)# 计算横向可容纳外星人数量
        # 计算可容纳多少行
        ship_height = self.ship.rect.height #获取飞船高度
        available_space_y = (self.settings.screen_height -
                                 (3 * alien_height) - ship_height) #计算垂直可用空间
        number_rows = available_space_y // (2 * alien_height) #计算可容纳行数

        
        for row_number in range(number_rows): #创建每行
            for alien_numer in range(number_aliens_x): #创建该行的每列
                #创建一个外星人并将其加入当前行
                self._create_alien(alien_numer,row_number)


    def _ship_hit(self): #响应飞船被撞
        """响应飞船北外星人撞到"""
        if self.stats.ships_left > 0: # 如果还有飞船
            self.stats.ships_left -= 1 #剩余飞船数减1
            
            # 清空余下外星人和子弹
            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新外星人,并将飞船放到屏幕底端中央
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5) #暂停0.5s,给玩家一点反应时间
        else: #飞船用光
            self.stats.game_active = False # 游戏结束

    def _update_aliens(self): #更新外星人群位置,状态
        """更新外星人编组中所有外星人的位置"""
        self._check_fleet_edges()
        self.aliens.update()
        #检测外星人与飞船之间的相撞
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            print("飞船于外星人相撞")
            self._ship_hit()
        self._check_aliens_bottom()
        

    def _check_fleet_edges(self): #检测外星人舰队触碰到左右边缘
        """有外星人到达边缘采取的措施"""
        for alien in self.aliens.sprites(): #遍历所有外星人
            if alien.check_edges(): #只要有一个触碰到边缘
                self._change_fleet_direction()# 改变所有外星人方向
                print("外星人碰到左右边界")
                break

    def _check_aliens_bottom(self): #检测外星人到达底端
        """检查是否有外星人到达了屏幕底端"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom: #如果飞船到达底端
                print("外星人到达底端")
                self._ship_hit()
                break

    def _change_fleet_direction(self): #下移后,改变外星人移动方向
        """整体下移改变方向"""
        for alien in self.aliens.sprites(): #对所有外星人
            alien.rect.y += self.settings.fleet_drop_speed #先向下移动
        self.settings.fleet_direction *= -1 #在改变方向
        




    def _update_screen(self): #更新屏幕
        """更新屏幕上的图像,并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)#每次循环时都重新绘制屏幕
        self.ship.blitme()#绘制飞船
        for bullet in self.bullets.sprites():#遍历编组的所有精灵
            bullet.draw_bullet()#绘制每个子弹
        self.aliens.draw(self.screen)#对外星人编组内所有成员在游戏屏幕上绘制

        # 如果游戏处于非活动状态, 就绘制按钮
        # 让按钮位于其他游戏元素上面, 所以最后再绘制按钮
        if not self.stats.game_active:
            self.play_button.draw_button()

        #让最近绘制的屏幕可见
        pygame.display.update()#切换到新屏幕



    def run_game(self): #游戏主循环
        """开始游戏主循环"""
        while True:
            self._check_events()#检测事件
            if self.stats.game_active: #以下代码尽在游戏处在活动状态时执行
                self.ship.update()#更新飞船位置
                self._update_bullets()#更新子弹
                self._update_aliens()# 更新外星人
            self._update_screen()#更新屏幕


if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()#创建游戏实例
    ai.run_game()#运行游戏
