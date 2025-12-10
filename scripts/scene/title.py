import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition.fade import FadeTransition, FadeMode
from scripts.transition.slide import SlideTransition, SlideDirection
from scripts.transition.wipe import WipeTransition, WipeDirection
from scripts.transition.blind import BlindTransition, BlindDirection
from scripts.transition.circle_wipe import CircleWipeTransition, CircleWipeMode
from scripts.transition.puzzle import PuzzleTransition
from scripts.transition.rotate_wipe import RotateWipeTransition, RotateWipeDirection


class TitleScene(Scene):
    """
    タイトルシーン
    Args:
        game (Game): ゲームオブジェクト
        manager (SceneManager): シーンマネージャー
    """
    
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager
        self.font = pygame.font.SysFont(None, 64)
        self.small_font = pygame.font.SysFont(None, 32)

        self.title_text = self.font.render("Title Scene", True, (255, 255, 255))
        self.fade_scene_text = self.small_font.render("w: Go to Fade Scene", True, (255, 255, 255))
        self.slide_scene_text = self.small_font.render("a: Go to Slide Scene", True, (255, 255, 255))
        self.wipe_scene_text = self.small_font.render("s: Go to Wipe Scene", True, (255, 255, 255))
        self.blind_scene_text = self.small_font.render("d: Go to Blind Scene", True, (255, 255, 255))
        self.circle_wipe_text = self.small_font.render("up: Go to Circle Wipe Scene", True, (255, 255, 255))
        self.puzzle_text = self.small_font.render("down: Go to Puzzle Scene", True, (255, 255, 255))
        self.rotate_slide_text = self.small_font.render("left: Go to Rotate Slide Scene", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        if self.game.inputs["w"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=0.5, mode=FadeMode.OUT)
            )
        elif self.game.inputs["a"]:
            self.manager.change_scene(
                SceneID.SLIDE,
                transition=SlideTransition(duration=0.5, direction=SlideDirection.LEFT)
            )
        elif self.game.inputs["s"]:
            self.manager.change_scene(
                SceneID.WIPE,
                transition=WipeTransition(duration=0.5, direction=WipeDirection.LEFT)
            )
        elif self.game.inputs["d"]:
            self.manager.change_scene(
                SceneID.BLIND,
                transition=BlindTransition(duration=0.5, direction=BlindDirection.LEFT)
            )
        elif self.game.inputs["up"]:
            self.manager.change_scene(
                SceneID.CIRCLE_WIPE,
                transition=CircleWipeTransition(duration=0.7, mode=CircleWipeMode.OPEN)
            )
        elif self.game.inputs["down"]:
            self.manager.change_scene(
                SceneID.PUZZLE,
                transition=PuzzleTransition(duration=0.8, cols=8, rows=6, seed=None)
            )
        elif self.game.inputs["left"]:
            self.manager.change_scene(
                SceneID.ROTATE_WIPE,
                transition=RotateWipeTransition(duration=0.7, direction=RotateWipeDirection.LEFT)
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.fade_scene_text, (50, 150))
        surface.blit(self.slide_scene_text, (50, 200))
        surface.blit(self.wipe_scene_text, (50, 250))
        surface.blit(self.blind_scene_text, (50, 300))
        surface.blit(self.circle_wipe_text, (50, 350))
        surface.blit(self.puzzle_text, (50, 400))
        surface.blit(self.rotate_slide_text, (50, 450))
