import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition.zoom import ZoomTransition, ZoomMode


class ZoomScene(Scene):
    """
    ズームシーンクラス

    Args:
        game (Game): ゲームオブジェクト
        manager (SceneManager): シーンマネージャー
    """
    
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager

        self.font = pygame.font.SysFont(None, 64)
        self.title_text = self.font.render("Title Scene", True, (255, 255, 255))

        self.small_font = pygame.font.SysFont(None, 32)
        self.back_text = self.small_font.render("Esc: Back to Title", True, (255, 255, 255))
        self.zoom_in_text = self.small_font.render("Up: Zoom In Transition", True, (255, 255, 255))
        self.zoom_out_text = self.small_font.render("Down: Zoom Out Transition", True, (255, 255, 255))
        self.zoom_inout_text = self.small_font.render("Left: Zoom InOut Transition", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        # タイトルに戻る
        if self.game.inputs["esc"]:
            self.manager.change_scene(SceneID.TITLE)
        # ズームイン
        if self.game.inputs["up"]:
            self.manager.change_scene(
                SceneID.ZOOM,
                transition=ZoomTransition(duration=0.8, mode=ZoomMode.IN)
            )
        # ズームアウト
        if self.game.inputs["down"]:
            self.manager.change_scene(
                SceneID.ZOOM,
                transition=ZoomTransition(duration=0.8, mode=ZoomMode.OUT)
            )
        # ズームインアウト
        if self.game.inputs["left"]:
            self.manager.change_scene(
                SceneID.ZOOM,
                transition=ZoomTransition(duration=1.6, mode=ZoomMode.INOUT)
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.back_text, (50, 150))
        surface.blit(self.zoom_in_text, (50, 200))
        surface.blit(self.zoom_out_text, (50, 250))
        surface.blit(self.zoom_inout_text, (50, 300))
