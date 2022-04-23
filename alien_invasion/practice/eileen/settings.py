class Settings:
    """存储游戏中所涉及的设置(set)相关的工作"""
    def __init__(self) -> None:
        """初始化游戏设置"""
        #屏幕相关设置
        self.screen_width=1000
        self.screen_height=800
        self.bg_color=(230,230,230)
        self.eileen_speed=2
