import pygame
from scripts.scene.base import Scene
from scripts.scene.ids import SceneID
from scripts.transition.fade import FadeTransition
from scripts.transition.wipe import WipeTransition


class GameScene(Scene):
    def __init__(self, game, manager):
        self.game = game
        self.manager = manager
        self.font = pygame.font.SysFont(None, 48)

        self.title_text = self.font.render("Game Scene", True, (255, 255, 255))
        self.info_text = self.font.render("ESC: Back to Title", True, (255, 255, 255))

    def handle(self):
        # ホワイトフェード遷移
        if self.game.inputs["enter"]:
            self.manager.goto(
                SceneID.TITLE,
                transition=FadeTransition(duration=0.5, mode="black")
            )

        # ワイプ遷移
        if self.game.inputs["w"]:
            self.manager.goto(
                SceneID.TITLE,
                transition=WipeTransition(duration=0.5, direction="left")
            )
            
    def update(self, dt):
        pass

    def render(self, surface):
        surface.fill((0, 80, 0))
        surface.blit(self.title_text, (50, 50))
        surface.blit(self.info_text, (50, 120))
