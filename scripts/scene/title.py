import pygame
from scripts.constants import GameConstants
from scripts.scene import Scene, SceneID
from scripts.transition import FadeTransition, FadeMode


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

    def handle(self):
        if self.game.inputs["w"]:
            self.manager.change_scene(
                SceneID.FADE,
                transition=FadeTransition(duration=0.5, mode=FadeMode.OUT)
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill(GameConstants.BG_COLORS["title"])
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.fade_scene_text, (50, 150))
