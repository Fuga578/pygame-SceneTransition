import pygame
from scripts.transition.base import Transition


class WipeTransition(Transition):
    def __init__(self, duration=0.5, direction="left"):
        super().__init__(duration)
        self.direction = direction

    def render(self, surface, old_surface, new_surface):
        t = self.elapsed / self.duration  # 0→1
        w, h = surface.get_size()

        # old はそのまま敷く
        surface.blit(old_surface, (0, 0))

        # new の表示範囲を決める
        if self.direction == "left":
            # 左から右へ広がる
            width = int(w * t)
            if width <= 0:
                return
            rect = pygame.Rect(0, 0, width, h)
            surface.blit(new_surface, (0, 0), rect)

        elif self.direction == "right":
            width = int(w * t)
            rect = pygame.Rect(w - width, 0, width, h)
            surface.blit(new_surface, (w - width, 0), rect)
