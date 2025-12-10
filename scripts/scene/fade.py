import pygame
import random
from scripts.scene import Scene, SceneID
from scripts.transition import FadeTransition, FadeMode


class FadeScene(Scene):
    """
    フェード遷移のデモシーン
    
    Args:
        game (Game): ゲームオブジェクト
        manager (SceneManager): シーンマネージャー
    """
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager

        self.font = pygame.font.SysFont(None, 64)
        self.title_text = self.font.render("Fade Scene", True, (255, 255, 255))

        self.small_font = pygame.font.SysFont(None, 32)
        self.back_text = self.small_font.render("Esc: Back to Title", True, (255, 255, 255))
        self.cross_fade_text = self.small_font.render("Enter: Cross Fade", True, (255, 255, 255))
        self.black_fade_out_text = self.small_font.render("w: Black Fade Out", True, (255, 255, 255))
        self.black_fade_in_text = self.small_font.render("a: Black Fade In", True, (255, 255, 255))
        self.black_fade_inout_text = self.small_font.render("s: Black Fade InOut", True, (255, 255, 255))
        self.white_fade_out_text = self.small_font.render("up: White Fade Out", True, (255, 255, 255))
        self.white_fade_in_text = self.small_font.render("down: White Fade In", True, (255, 255, 255))
        self.white_fade_inout_text = self.small_font.render("left: White Fade InOut", True, (255, 255, 255))
        
        self.bg_color = (random.randint(0, 150), random.randint(0, 150), random.randint(0, 150))

    def handle(self):
        # タイトルに戻る
        if self.game.inputs["esc"]:
            self.manager.change_scene(SceneID.TITLE)
        # クロスフェード
        elif self.game.inputs["enter"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=1.0, mode=FadeMode.CROSS)
            )
        # 黒フェードアウト
        elif self.game.inputs["w"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=1.0, mode=FadeMode.OUT, color=(0, 0, 0))
            )
        # 黒フェードイン
        elif self.game.inputs["a"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=1.0, mode=FadeMode.IN, color=(0, 0, 0))
            )
        # 黒フェードインアウト
        elif self.game.inputs["s"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=1.0, mode=FadeMode.INOUT, color=(0, 0, 0))
            )
        # 白フェードアウト
        elif self.game.inputs["up"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=1.0, mode=FadeMode.OUT, color=(255, 255, 255))
            )
        # 白フェードイン
        elif self.game.inputs["down"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=1.0, mode=FadeMode.IN, color=(255, 255, 255))
            )
        # 白フェードインアウト
        elif self.game.inputs["left"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=1.0, mode=FadeMode.INOUT, color=(255, 255, 255))
            )
            
    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(self.bg_color)
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.back_text, (50, 100))
        surface.blit(self.cross_fade_text, (50, 150))
        surface.blit(self.black_fade_out_text, (50, 200))
        surface.blit(self.black_fade_in_text, (50, 250))
        surface.blit(self.black_fade_inout_text, (50, 300))
        surface.blit(self.white_fade_out_text, (50, 350))
        surface.blit(self.white_fade_in_text, (50, 400))
        surface.blit(self.white_fade_inout_text, (50, 450))