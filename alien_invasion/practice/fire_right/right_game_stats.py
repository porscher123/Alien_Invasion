from pygame import init


class GameStats:
    def __init__(self, ai_game) -> None:
        self.settings = ai_game.settings
        self.ship_hit = 0 #*统计飞船被撞次数
        self.aliens_killed = 0 #*统计被击杀的外星人数量
        self.game_active = True