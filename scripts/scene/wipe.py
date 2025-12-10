import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition.wipe import WipeTransition, WipeDirection


class WipeScene(Scene):
    """
    ワイプ遷移のデモシーン
    
    Args:
        game (Game): ゲームオブジェクト
        manager (SceneManager): シーンマネージャー
    """
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager

        self.font = pygame.font.SysFont(None, 64)
        self.title_text = self.font.render("Wipe Scene", True, (255, 255, 255))

        self.small_font = pygame.font.SysFont(None, 32)
        self.back_text = self.small_font.render("Esc: Back to Title", True, (255, 255, 255))
        self.up_wipe_text = self.small_font.render("up: Wipe Up", True, (255, 255, 255))
        self.down_wipe_text = self.small_font.render("down: Wipe Down", True, (255, 255, 255))
        self.left_wipe_text = self.small_font.render("left: Wipe Left", True, (255, 255, 255))
        self.right_wipe_text = self.small_font.render("right: Wipe Right", True, (255, 255, 255))
        self.center_horizontal_wipe_text = self.small_font.render("w: Wipe Center Horizontal", True, (255, 255, 255))
        self.center_vertical_wipe_text = self.small_font.render("a: Wipe Center Vertical", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        # タイトルに戻る
        if self.game.inputs["esc"]:
            self.manager.change_scene(SceneID.TITLE)
        # 上方向にワイプ
        elif self.game.inputs["up"]:
            self.manager.change_scene(SceneID.WIPE, WipeTransition(direction=WipeDirection.UP, duration=1.0))
        # 下方向にワイプ
        elif self.game.inputs["down"]:
            self.manager.change_scene(SceneID.WIPE, WipeTransition(direction=WipeDirection.DOWN, duration=1.0))
        # 左方向にワイプ
        elif self.game.inputs["left"]:
            self.manager.change_scene(SceneID.WIPE, WipeTransition(direction=WipeDirection.LEFT, duration=1.0))
        # 右方向にワイプ
        elif self.game.inputs["right"]:
            self.manager.change_scene(SceneID.WIPE, WipeTransition(direction=WipeDirection.RIGHT, duration=1.0))
        # 中央から左右にワイプ
        elif self.game.inputs["w"]:
            self.manager.change_scene(SceneID.WIPE, WipeTransition(direction=WipeDirection.CENTER_HORIZONTAL, duration=1.0))
        # 中央から上下にワイプ
        elif self.game.inputs["a"]:
            self.manager.change_scene(SceneID.WIPE, WipeTransition(direction=WipeDirection.CENTER_VERTICAL, duration=1.0))

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.back_text, (50, 100))
        surface.blit(self.up_wipe_text, (50, 150))
        surface.blit(self.down_wipe_text, (50, 200))
        surface.blit(self.left_wipe_text, (50, 250))
        surface.blit(self.right_wipe_text, (50, 300))
        surface.blit(self.center_horizontal_wipe_text, (50, 350))
        surface.blit(self.center_vertical_wipe_text, (50, 400))