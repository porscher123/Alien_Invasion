class Settings:
    """存储游戏中所涉及的设置(set)相关的工作"""
    def __init__(self) -> None:
        """初始化游戏设置"""

        #?屏幕相关设置
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed = 1.5

        #?子弹相关设置
        self.bullet_speed = 1.0
        self.bullet_width = 1
        self.bullet_height = 500
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #?外星人
        self.alien_speed = 0 #* 外星人速度
        self.alien_drop = 50 #*外星人碰到边缘后横向移动距离
        self.aliens_target = 50 #*杀够50个外星人游戏结束