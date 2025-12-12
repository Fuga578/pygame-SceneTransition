import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.effect import ScreenShakeEffect
from scripts.transition import FadeTransition, FadeMode, \
    SlideTransition, SlideDirection, WipeTransition, WipeDirection, \
    BlindTransition, BlindDirection, CircleWipeTransition, CircleWipeMode, \
    PuzzleTransition, RotateWipeTransition, RotateWipeDirection, \
    ZoomTransition, ZoomMode, MosaicTransition, MosaicMode, \
    ScanlineTransition, ScanlineDirection, FlipTransition, FlipAxis
from scripts.scene.overlay import PauseScene


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
        self.pause_text = self.small_font.render("p: Pause", True, (255, 255, 255))
        self.fade_scene_text = self.small_font.render("w: Go to Fade Scene", True, (255, 255, 255))
        self.slide_scene_text = self.small_font.render("a: Go to Slide Scene", True, (255, 255, 255))
        self.wipe_scene_text = self.small_font.render("s: Go to Wipe Scene", True, (255, 255, 255))
        self.blind_scene_text = self.small_font.render("d: Go to Blind Scene", True, (255, 255, 255))
        self.circle_wipe_text = self.small_font.render("up: Go to Circle Wipe Scene", True, (255, 255, 255))
        self.puzzle_text = self.small_font.render("down: Go to Puzzle Scene", True, (255, 255, 255))
        self.rotate_slide_text = self.small_font.render("left: Go to Rotate Slide Scene", True, (255, 255, 255))
        self.zoom_text = self.small_font.render("right: Go to Zoom Scene", True, (255, 255, 255))
        self.screen_shake_text = self.small_font.render("Enter: Screen Shake", True, (255, 255, 255))
        self.mosaic_text = self.small_font.render("z: Go to Mosaic Scene", True, (255, 255, 255))
        self.scanline_text = self.small_font.render("x: Go to Scanline Scene", True, (255, 255, 255))
        self.flip_text = self.small_font.render("c: Go to Flip Scene", True, (255, 255, 255))

        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))
        
        self.screen_shake_effect = ScreenShakeEffect()

    def handle(self):
        if self.game.inputs["p"]:
            self.manager.push_overlay(PauseScene(self.game, self.manager))
        elif self.game.inputs["q"]:
            self.game.exit()
        elif self.game.inputs["w"]:
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
        elif self.game.inputs["right"]:
            self.manager.change_scene(
                SceneID.ZOOM,
                transition=ZoomTransition(duration=0.8, mode=ZoomMode.IN)
            )
        elif self.game.inputs["enter"]:
            self.screen_shake_effect.start()
        elif self.game.inputs["z"]:
            self.manager.change_scene(
                SceneID.MOSAIC,
                transition=MosaicTransition(duration=1.0, mode=MosaicMode.INOUT)
            )
        elif self.game.inputs["x"]:
            self.manager.change_scene(
                SceneID.SCANLINE,
                transition=ScanlineTransition(direction=ScanlineDirection.VERTICAL)
            )
        elif self.game.inputs["c"]:
            self.manager.change_scene(
                SceneID.FLIP,
                transition=FlipTransition(axis=FlipAxis.Y)
            )

    def update(self, dt):
        self.screen_shake_effect.update(dt)

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.pause_text, (50, 100))
        surface.blit(self.fade_scene_text, (50, 140))
        surface.blit(self.slide_scene_text, (50, 180))
        surface.blit(self.wipe_scene_text, (50, 220))
        surface.blit(self.blind_scene_text, (50, 260))
        surface.blit(self.circle_wipe_text, (50, 300))
        surface.blit(self.puzzle_text, (50, 340))
        surface.blit(self.rotate_slide_text, (50, 380))
        surface.blit(self.zoom_text, (50, 420))
        surface.blit(self.screen_shake_text, (50, 460))
        surface.blit(self.mosaic_text, (50, 500))
        surface.blit(self.scanline_text, (50, 540))
        surface.blit(self.flip_text, (50, 580))

        self.screen_shake_effect.apply(surface)