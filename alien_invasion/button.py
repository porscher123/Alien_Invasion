import pygame.font

class Button:
    # msgs是按钮要显示的文本
    def __init__(self, ai_game, msg) -> None:
        """#初始化按钮的属性"""
        # 相当于把按钮添加到游戏屏幕上
        self.screen = ai_game.screen    # 设置按钮的屏幕为游戏窗口的屏幕
        self.screen_rect = self.screen.get_rect()   # 设置按钮窗口矩形为游戏的窗口矩形

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 200, 50   # 设置按钮的宽高
        self.button_color = (0, 255, 0) # 设置按钮为绿色背景
        self.text_color = (255, 255, 255)   # 设置按钮上文字为白色
        self.font = pygame.font.SysFont(None, 48)   # 字体为默认, 字号48

        # 创建按钮的rect对象, 并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)  # 创建按钮的rect对象
        self.rect.center = self.screen_rect.center # 使按钮的rect在游戏窗口的rect的中间
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """将msg渲染为图像, 并使其在按钮上居中"""
        # font.render()将文本渲染成图像     源文本   bool值表示开启反锯齿, 文本颜色和背景色(默认透明)
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        # 将文本设置到按钮中心
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center 
    
    def draw_button(self):
        # 绘制一个用颜色填充的按钮, 再绘制文本
        self.screen.fill(self.button_color, self.rect) # 绘制表示按钮的矩形
        self.screen.blit(self.msg_img, self.msg_img_rect) # 向按钮的矩形传递文本图像和文本图像的rect

