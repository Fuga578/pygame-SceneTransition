import pygame
from enum import Enum
from scripts.transition import Transition


class BlindDirection(Enum):
    """
    ブラインド方向

    UP: 上 -> 下にブラインド
    DOWN: 下 -> 上にブラインド
    LEFT: 左 -> 右にブラインド
    RIGHT: 右 -> 左にブラインド
    """
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"


class BlindTransition(Transition):
    """
    ブラインド遷移クラス

    Args:
        duration (float): 遷移時間（秒）
        strip_count (int): ブラインドの本数

        direction (BlindDirection): ブラインド方向
    """
    def __init__(self, duration=0.6, strip_count=10, direction=BlindDirection.LEFT):
        super().__init__(duration)
        self.strip_count = max(1, strip_count)
        self.direction = direction

    def render(self, surface, old_surface, new_surface):
        t = max(0.0, min(1.0, self.elapsed / self.duration))

        w, h = surface.get_size()
        surface.blit(old_surface, (0, 0))

        # 左 -> 右に開く
        if self.direction is BlindDirection.LEFT:
            strip_h = h // self.strip_count
            for i in range(self.strip_count):
                y = i * strip_h

                local_t = self._local_t(i, t)
                width = int(w * local_t)
                if width > 0:
                    rect = pygame.Rect(0, y, width, strip_h)
                    surface.blit(new_surface, (0, y), rect)

        # 右 -> 左に開く
        elif self.direction is BlindDirection.RIGHT:
            strip_h = h // self.strip_count
            for i in range(self.strip_count):
                y = i * strip_h

                local_t = self._local_t(i, t)
                width = int(w * local_t)
                if width > 0:
                    rect = pygame.Rect(w - width, y, width, strip_h)
                    surface.blit(new_surface, (w - width, y), rect)

        # 上 -> 下に開く
        elif self.direction is BlindDirection.UP:
            strip_w = w // self.strip_count
            for i in range(self.strip_count):
                x = i * strip_w

                local_t = self._local_t(i, t)
                height = int(h * local_t)
                if height > 0:
                    rect = pygame.Rect(x, 0, strip_w, height)
                    surface.blit(new_surface, (x, 0), rect)

        # 下 -> 上に開く
        elif self.direction is BlindDirection.DOWN:
            strip_w = w // self.strip_count
            for i in range(self.strip_count):
                x = i * strip_w

                local_t = self._local_t(i, t)
                height = int(h * local_t)
                if height > 0:
                    rect = pygame.Rect(x, h - height, strip_w, height)
                    surface.blit(new_surface, (x, h - height), rect)

    def _local_t(self, i, t):
        """時間差処理を共通化"""
        offset = (i / self.strip_count) * 0.5
        local_t = (t - offset) / 0.5
        return max(0.0, min(1.0, local_t))
