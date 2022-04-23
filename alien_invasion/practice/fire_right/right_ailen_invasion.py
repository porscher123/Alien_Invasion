#导入模块
from random import randint
import sys
from time import sleep
from right_game_stats import GameStats
from right_bullet import Bullet
import pygame
from right_settings import Settings
from right_ship import Ship
from right_alien import Alien
#创建游戏类
class AlienInvasion:
    """管理游戏资源和行为的类"""
 
    def __init__(self) -> None:
        """初始化游戏并创建游戏资源"""
        pygame.init() #c初始化背景设置
        self.settings = Settings()#创建设置对象,赋给游戏的设置属性
        self.stats = GameStats(self)
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#指定尺寸创建一个窗口,赋给游戏的screen属性
        pygame.display.set_caption("Alien Invasion")
        self.ship=Ship(self)#创建飞船(传入self),赋给属性ship
        #创建存储子弹的编组
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()


    def _check_keydown_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down=True
        elif event.key == pygame.K_SPACE:#按下空格键
            self._fire_bullet()
        elif event.key == pygame.K_q:#按Q键
            sys.exit()#退出程序
        elif event.key == pygame.K_m:
            self.settings.alien_speed = 1
    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_UP:
            self.ship.moving_up=False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down=False
        
    def _check_events(self):
        """监视键盘和鼠标事件"""
        for event in pygame.event.get():#遍历事件列表
            if event.type == pygame.QUIT:#用户点击关闭按钮使,检测到QUIT事件
                sys.exit()#调用系统函数关闭窗口
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)#检测按下右方向键
            elif event.type ==pygame.KEYUP:
                self._check_keyup_events(event)#检测释放右方向键
                    
    def _fire_bullet(self): 
        """创建一颗子弹,并将其加入编组"""
        if len(self.bullets) < self.settings.bullets_allowed:#判断当前编组内子弹数量是否在允许范围内
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)


    def _create_alien(self, row, column): #*在某行某列创建一个外星人
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        # 计算放置该外星人的坐标
        alien.x = alien_width +  2 * alien_width * column #* 乘列数获得x坐标
        alien.y = alien_height +  2* alien_height * row  #* 乘行数获得y坐标
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien) 

    def _create_fleet(self): #* 创建一个外星人编队
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size 
        #* 可修改改变行列容纳数量,纵向多,横向少
        available_space_x = self.settings.screen_width - (2 * alien_width) #* 计算横向可用空间    
        available_space_y = self.settings.screen_height - (2 * alien_height) #*计算垂直可用空间

        number_aliens_x = available_space_x // (2 * alien_width) # 计算横向可容纳外星人数量
        number_rows = available_space_y // ( 2* alien_height) #计算可容纳行数

        #* 随机布局
        alien_number = 10 #* 随机生成多少个外星人
        for num in range(alien_number):
            row = randint(0,number_rows) #* 随机生成行
            column = randint(3,number_aliens_x) #* 随机讽刺列数(列数起点可调)
            print(row,column)
            self._create_alien(row ,column) #* 在某行某列创建一个外星人

        #* 矩形布局
        # for row in range(number_rows): #创建每行
        #     for column in range(number_aliens_x): #创建该行的每列
        #         #创建一个外星人并将其加入当前行
        #         self._create_alien(column,row)


    def _check_bullet_alien_collision(self):
        """检查子弹与外星人碰撞"""
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,False,True
        )
        self.stats.aliens_killed += collisions.__len__() #*获取当前击杀的外星人数量
        if self.stats.aliens_killed >= self.settings.aliens_target: #*数量大于等于目标数量
            self.stats.game_active =False #*游戏结束

        if not self.aliens: #*如果外星人被杀光
            self.bullets.empty() #清空子弹
            self._create_fleet() #生成新的外星人群

    def _check_fleet_edges(self): #!谁碰到边界改变谁的方向
        # flag = 0
        for alien in self.aliens.sprites():
            if alien.check_edges():
                alien.direction *= -1
                alien.rect.x -= self.settings.alien_drop
        # if flag:
        #     for alien in self.aliens.sprites():
                
    def _ship_hit(self): #*响应飞船碰撞
        self.stats.ship_hit += 1
        if self.stats.ship_hit <= 3: #*飞船被撞击数量小于3时游戏才能正常进行
            self.bullets.empty()
            self.aliens.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.1)
        else:
            self.stats.game_active = False
        

    def _check_aliens_left(self): #*检测外星人到达屏幕左端
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.left <= screen_rect.left:
                self._ship_hit() #*同飞船与外星人相撞对待        


    def _update_bullets(self): #*更新子弹
        """更新子弹位置,并删除消失子弹"""
        self.bullets.update()#更新子弹组的位置,对编组操作,即对组内每个成员操作
        #删除消失的子弹
        for bullet in self.bullets.copy():#遍历编组的副本
            if bullet.rect.left > self.screen.get_rect().width: #如果子弹左边框超过屏幕宽度,即消失
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _update_aliens(self): #*更新外星人位置,检测外星人状态
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens): #* 如果飞船与外星人相撞
            self._ship_hit()

    def _update_screen(self): #*更新屏幕
        """更新屏幕上的图像,并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)#每次循环时都重新绘制屏幕
        self.ship.blitme()#绘制飞船
        for bullet in self.bullets.sprites():#遍历编组的所有精灵
            bullet.draw_bullet()#绘制每个精灵
        self.aliens.draw(self.screen)
        #让最近绘制的屏幕可见
        pygame.display.flip()#切换到新屏幕



    def run_game(self): #* 游戏主循环
        """开始游戏主循环"""
        while True:
            self._check_events()#检测事件
            if self.stats.game_active:
                self.ship.update()#更新飞船位置
                self._update_bullets()#更新子弹
                self._update_aliens()
            self._update_screen()#更新屏幕

if __name__ == '__main__':
    #创建游戏实例并运行游戏
    ai = AlienInvasion()#创建游戏实例
    ai.run_game()#运行游戏
