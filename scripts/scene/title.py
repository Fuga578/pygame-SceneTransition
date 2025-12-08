import pygame
from scripts.scene.base import Scene
from scripts.scene.ids import SceneID
from scripts.transition.fade import FadeTransition
from scripts.transition.wipe import WipeTransition


class TitleScene(Scene):
    
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager
        self.font = pygame.font.SysFont(None, 64)
        self.small_font = pygame.font.SysFont(None, 32)

        self.title_text = self.font.render("Title Scene", True, (255, 255, 255))
        self.info_text = self.small_font.render("Press Enter to Start", True, (255, 255, 255))

    def handle(self):
        if self.game.inputs["enter"]:
            self.manager.goto(
                SceneID.GAME,
                transition=FadeTransition(duration=0.5, mode="black")
            )

        # W キーでワイプ遷移したい場合
        if self.game.inputs["w"]:
            self.manager.goto(
                SceneID.GAME,
                transition=WipeTransition(duration=0.5, direction="left")
            )

    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill((0, 0, 80))

        surface.blit(self.title_text, (50, 50))
        surface.blit(self.info_text, (50, 140))
