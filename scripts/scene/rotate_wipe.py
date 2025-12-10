import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition.rotate_wipe import RotateWipeTransition, RotateWipeDirection


class RotateWipeScene(Scene):
    """
    回転ワイプシーン

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
        self.up_slide_text = self.small_font.render("Up: Rotate Slide Up", True, (255, 255, 255))
        self.down_slide_text = self.small_font.render("Down: Rotate Slide Down", True, (255, 255, 255))
        self.left_slide_text = self.small_font.render("Left: Rotate Slide Left", True, (255, 255, 255))
        self.right_slide_text = self.small_font.render("Right: Rotate Slide Right", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        # タイトルに戻る
        if self.game.inputs["esc"]:
            self.manager.change_scene(SceneID.TITLE)
        # 上方向
        elif self.game.inputs["up"]:
            self.manager.change_scene(
                SceneID.ROTATE_WIPE,
                RotateWipeTransition(duration=1.0, direction=RotateWipeDirection.UP, start_angle=90)
            )
        # 下方向
        elif self.game.inputs["down"]:
            self.manager.change_scene(
                SceneID.ROTATE_WIPE,
                RotateWipeTransition(duration=1.0, direction=RotateWipeDirection.DOWN, start_angle=90)
            )
        # 左方向
        elif self.game.inputs["left"]:
            self.manager.change_scene(
                SceneID.ROTATE_WIPE,
                RotateWipeTransition(duration=1.0, direction=RotateWipeDirection.LEFT, start_angle=90)
            )
        # 右方向
        elif self.game.inputs["right"]:
            self.manager.change_scene(
                SceneID.ROTATE_WIPE,
                RotateWipeTransition(duration=1.0, direction=RotateWipeDirection.RIGHT, start_angle=90)
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.back_text, (50, 150))
        surface.blit(self.up_slide_text, (50, 200))
        surface.blit(self.down_slide_text, (50, 250))
        surface.blit(self.left_slide_text, (50, 300))
        surface.blit(self.right_slide_text, (50, 350))        
