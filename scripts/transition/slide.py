import pygame
from enum import Enum
from scripts.transition import Transition


class SlideDirection(Enum):
    """
    スライド方向
    """
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    

class SlideTransition(Transition):
    """
    スライド遷移クラス

    Args:
        duration (float): 遷移時間（秒）
        direction (SlideDirection): スライド方向
    """
    def __init__(self, duration=0.5, direction=SlideDirection.LEFT):
        super().__init__(duration)
        self.direction = direction

    def render(self, surface, old_surface, new_surface):
        t = self.elapsed / self.duration
        t = max(0.0, min(1.0, t))
        w, h = surface.get_size()

        if self.direction == SlideDirection.LEFT:
            # old が左に押し出されて、右から new が入ってくる
            offset = int(t * w)
            surface.blit(old_surface, (-offset, 0))
            surface.blit(new_surface, (w - offset, 0))

        elif self.direction == SlideDirection.RIGHT:
            offset = int(t * w)
            surface.blit(old_surface, (offset, 0))
            surface.blit(new_surface, (-w + offset, 0))

        elif self.direction == SlideDirection.UP:
            offset = int(t * h)
            surface.blit(old_surface, (0, -offset))
            surface.blit(new_surface, (0, h - offset))

        elif self.direction == SlideDirection.DOWN:
            offset = int(t * h)
            surface.blit(old_surface, (0, offset))
            surface.blit(new_surface, (0, -h + offset))
