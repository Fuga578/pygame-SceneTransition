import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition import ScanlineTransition, ScanlineDirection


class ScanlineScene(Scene):
    """
    スキャンラインシーンクラス

    Args:
        game (Game): ゲームオブジェクト
        manager (SceneManager): シーンマネージャー
    """
    
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager

        self.font = pygame.font.SysFont(None, 64)
        self.title_text = self.font.render("Scanline Scene", True, (255, 255, 255))

        self.small_font = pygame.font.SysFont(None, 32)
        self.back_text = self.small_font.render("Esc: Back to Title", True, (255, 255, 255))
        self.vertical_scan_text = self.small_font.render("Up/Down: Vertical Scanline", True, (255, 255, 255))   
        self.horizontal_scan_text = self.small_font.render("Left/Right: Horizontal Scanline", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        # タイトルに戻る
        if self.game.inputs["esc"]:
            self.manager.change_scene(SceneID.TITLE)
        # 横スキャン
        elif self.game.inputs["left"] or self.game.inputs["right"]:
            self.manager.change_scene(
                SceneID.SCANLINE,
                ScanlineTransition(direction=ScanlineDirection.VERTICAL),
            )
        # 縦スキャン
        elif self.game.inputs["up"] or self.game.inputs["down"]:
            self.manager.change_scene(
                SceneID.SCANLINE,
                ScanlineTransition(direction=ScanlineDirection.HORIZONTAL),
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.back_text, (50, 150))
        surface.blit(self.vertical_scan_text, (50, 200))
        surface.blit(self.horizontal_scan_text, (50, 250))