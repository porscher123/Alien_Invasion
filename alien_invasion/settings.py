class Settings:
    """存储游戏中所涉及的设置(set)相关的工作"""
    def __init__(self) -> None:
        """初始化游戏设置"""

        #?屏幕相关设置
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230,230,230)
        

        #?子弹相关设置
        self.bullet_speed = 1
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #?外星人相关
        self.alien_speed = 1.5
        self.fleet_drop_speed = 50 #撞到边缘后,下降的速度
        self.fleet_direction = 1 # 1->向右移动  -1->向左移动

        #?飞船相关
        self.ship_speed = 1
        self.ship_limit = 3