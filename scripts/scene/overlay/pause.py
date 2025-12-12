import pygame
from scripts.scene.base import Scene

class PauseScene(Scene):
    def __init__(self, game, manager, bg_color=(0, 0, 0, 160)):
        self.game = game
        self.manager = manager
        self.bg_color = bg_color
        self.font = pygame.font.SysFont(None, 64)

    def handle(self):
        if self.game.inputs["esc"]:
            self.manager.pop_overlay()

    def update(self, dt): 
        pass

    def render(self, surface):
        overlay = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 160))
        surface.blit(overlay, (0, 0))
        surface.blit(self.font.render("PAUSE", True, (255,255,255)), (50, 50))
