class GameStats:
    """跟踪游戏统计信息"""
    def __init__(self, ai_game) -> None:
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.game_active = False    # 让游戏一开始处于非活动状态
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit