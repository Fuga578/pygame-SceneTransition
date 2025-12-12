import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition import CircleWipeTransition, CircleWipeMode


class CircleWipeScene(Scene):
    """
    サークルワイプシーン

    Args:
        game (Game): ゲームオブジェクト
        manager (SceneManager): シーンマネージャー
    """
    
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager

        self.font = pygame.font.SysFont(None, 64)
        self.title_text = self.font.render("Circle Wipe Scene", True, (255, 255, 255))

        self.small_font = pygame.font.SysFont(None, 32)
        self.back_text = self.small_font.render("Esc: Back to Title", True, (255, 255, 255))
        self.circle_open_text = self.small_font.render("Up: Open", True, (255, 255, 255))
        self.circle_close_text = self.small_font.render("Down: Close", True, (255, 255, 255))
        self.circle_close_open_text = self.small_font.render("Left: Close and Open", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        # タイトルに戻る
        if self.game.inputs["esc"]:
            self.manager.change_scene(SceneID.TITLE)
        # オープン
        elif self.game.inputs["up"]:
            self.manager.change_scene(
                SceneID.CIRCLE_WIPE,
                transition=CircleWipeTransition(duration=0.7, mode=CircleWipeMode.OPEN)
            )
        # クローズ
        elif self.game.inputs["down"]:
            self.manager.change_scene(
                SceneID.CIRCLE_WIPE,
                transition=CircleWipeTransition(duration=0.7, mode=CircleWipeMode.CLOSE)
            )
        # クローズ＋オープン
        elif self.game.inputs["left"]:
            self.manager.change_scene(
                SceneID.CIRCLE_WIPE,
                transition=CircleWipeTransition(duration=1.4, mode=CircleWipeMode.CLOSE_OPEN, bg_color=self.bg_color)
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.back_text, (50, 150))
        surface.blit(self.circle_open_text, (50, 200))
        surface.blit(self.circle_close_text, (50, 250))
        surface.blit(self.circle_close_open_text, (50, 300))