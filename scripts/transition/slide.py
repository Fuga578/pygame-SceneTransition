import pygame
from scripts.transition.base import Transition


class SlideTransition(Transition):
    def __init__(self, duration=0.5, direction="left"):
        """
        direction: "left", "right", "up", "down"
        old が押し出されて new がスライドイン
        """
        super().__init__(duration)
        self.direction = direction

    def render(self, surface, old_surface, new_surface):
        t = self.elapsed / self.duration
        t = max(0.0, min(1.0, t))
        w, h = surface.get_size()

        if self.direction == "left":
            # old が左に押し出されて、右から new が入ってくる
            offset = int(t * w)
            surface.blit(old_surface, (-offset, 0))
            surface.blit(new_surface, (w - offset, 0))

        elif self.direction == "right":
            offset = int(t * w)
            surface.blit(old_surface, (offset, 0))
            surface.blit(new_surface, (-w + offset, 0))

        elif self.direction == "up":
            offset = int(t * h)
            surface.blit(old_surface, (0, -offset))
            surface.blit(new_surface, (0, h - offset))

        elif self.direction == "down":
            offset = int(t * h)
            surface.blit(old_surface, (0, offset))
            surface.blit(new_surface, (0, -h + offset))
