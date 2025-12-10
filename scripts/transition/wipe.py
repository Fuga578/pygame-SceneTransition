import pygame
from enum import Enum
from scripts.transition import Transition


class WipeDirection(Enum):
    """
    ワイプの方向
    """
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    CENTER_HORIZONTAL = "center_horizontal"
    CENTER_VERTICAL = "center_vertical"


class WipeTransition(Transition):
    """
    ワイプ遷移クラス

    Args:
        duration (float): 遷移時間（秒）
        direction (WipeDirection): ワイプの方向
    """
    def __init__(self, duration=0.5, direction=WipeDirection.LEFT):
        super().__init__(duration)
        self.direction = direction

    def render(self, surface, old_surface, new_surface):
        t = self.elapsed / self.duration  # 0 -> 1
        t = max(0.0, min(1.0, t))

        w, h = surface.get_size()

        # old をまず描画
        surface.blit(old_surface, (0, 0))

        if self.direction == WipeDirection.LEFT:
            width = int(w * t)
            if width <= 0:
                return
            rect = pygame.Rect(0, 0, width, h)
            surface.blit(new_surface, (0, 0), rect)

        elif self.direction == WipeDirection.RIGHT:
            width = int(w * t)
            if width <= 0:
                return
            rect = pygame.Rect(w - width, 0, width, h)
            surface.blit(new_surface, (w - width, 0), rect)

        elif self.direction == WipeDirection.UP:
            height = int(h * t)
            if height <= 0:
                return
            rect = pygame.Rect(0, 0, w, height)
            surface.blit(new_surface, (0, 0), rect)

        elif self.direction == WipeDirection.DOWN:
            height = int(h * t)
            if height <= 0:
                return
            rect = pygame.Rect(0, h - height, w, height)
            surface.blit(new_surface, (0, h - height), rect)

        elif self.direction == WipeDirection.CENTER_HORIZONTAL:
            half_width = w // 2
            width = int(half_width * t)
            if width <= 0:
                return

            # 左側：中心から左へ広がる
            left_rect = pygame.Rect(half_width - width, 0, width, h)
            surface.blit(new_surface, (half_width - width, 0), left_rect)

            # 右側：中心から右へ広がる
            right_rect = pygame.Rect(half_width, 0, width, h)
            surface.blit(new_surface, (half_width, 0), right_rect)

        elif self.direction == WipeDirection.CENTER_VERTICAL:
            half_height = h // 2
            height = int(half_height * t)
            if height <= 0:
                return

            # 上側：中心から上へ広がる
            top_rect = pygame.Rect(0, half_height - height, w, height)
            surface.blit(new_surface, (0, half_height - height), top_rect)

            # 下側：中心から下へ広がる
            bottom_rect = pygame.Rect(0, half_height, w, height)
            surface.blit(new_surface, (0, half_height), bottom_rect)
