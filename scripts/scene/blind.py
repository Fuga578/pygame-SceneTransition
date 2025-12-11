import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition import BlindTransition, BlindDirection


class BlindScene(Scene):
    """
    ブラインドシーンクラス

    Args:
        game (Game): ゲームオブジェクト
        manager (SceneManager): シーンマネージャー
    """
    
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager
        self.font = pygame.font.SysFont(None, 64)
        self.title_text = self.font.render("Blind Scene", True, (255, 255, 255))

        self.small_font = pygame.font.SysFont(None, 32)
        self.back_text = self.small_font.render("Esc: Back to Title", True, (255, 255, 255))
        self.left_blind_text = self.small_font.render("left: Left Blind", True, (255, 255, 255))
        self.right_blind_text = self.small_font.render("right: Right Blind", True, (255, 255, 255))
        self.up_blind_text = self.small_font.render("up: Up Blind", True, (255, 255, 255))
        self.down_blind_text = self.small_font.render("down: Down Blind", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        # タイトルに戻る
        if self.game.inputs["esc"]:
            self.manager.change_scene(SceneID.TITLE)
        # 左方向ブラインド
        elif self.game.inputs["left"]:
            self.manager.change_scene(
                SceneID.BLIND,
                BlindTransition(direction=BlindDirection.LEFT, duration=1.0)
            )
        # 右方向ブラインド
        elif self.game.inputs["right"]:
            self.manager.change_scene(
                SceneID.BLIND,
                BlindTransition(direction=BlindDirection.RIGHT, duration=1.0)
            )
        # 上方向ブラインド
        elif self.game.inputs["up"]:
            self.manager.change_scene(
                SceneID.BLIND,
                BlindTransition(direction=BlindDirection.UP, duration=1.0)
            )
        # 下方向ブラインド
        elif self.game.inputs["down"]:
            self.manager.change_scene(
                SceneID.BLIND,
                BlindTransition(direction=BlindDirection.DOWN, duration=1.0)
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.back_text, (50, 150))
        surface.blit(self.left_blind_text, (50, 200))
        surface.blit(self.right_blind_text, (50, 250))
        surface.blit(self.up_blind_text, (50, 300))
        surface.blit(self.down_blind_text, (50, 350))
        
