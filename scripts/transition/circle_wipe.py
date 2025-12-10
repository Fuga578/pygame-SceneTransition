import math
import pygame
from enum import Enum
from scripts.transition import Transition


class CircleWipeMode(Enum):
    """
    円形ワイプモード

    OPEN       : 中央から外側に広がる
    CLOSE      : 外側から中央に縮む
    CLOSE_OPEN : 外側から中央に縮み、暗転後に中央から外側に広がる
    """
    OPEN = "open"
    CLOSE = "close"
    CLOSE_OPEN = "close_open"


class CircleWipeTransition(Transition):
    def __init__(
        self,
        duration: float = 0.7,
        center=None,
        mode: CircleWipeMode = CircleWipeMode.OPEN,
        bg_color=None,
    ):
        """
        Args:
            duration : 遷移時間（秒）
            center   : 円の中心座標 (x, y)。None なら画面中央。
            mode     : CircleWipeMode
            bg_color : 背景色（暗転色）
        """
        super().__init__(duration)
        self.center = center
        self.mode = mode
        self.bg_color = bg_color or (0, 0, 0)  # CLOSE_OPEN 用に黒をデフォルトにしておく

    def render(self, surface, old_surface, new_surface):
        t = max(0.0, min(1.0, self.elapsed / self.duration))
        w, h = surface.get_size()

        # 中心
        cx, cy = self.center if self.center is not None else (w // 2, h // 2)

        # 画面を覆える最大半径
        max_radius = int(math.hypot(w, h) / 2)

        if self.mode is CircleWipeMode.OPEN:
            radius = int(t * max_radius)  # 0 -> max
            base = old_surface            # 円の外側
            under = new_surface           # 円の内側

            # 外側
            surface.blit(base, (0, 0))

            # 内側（円形マスク）
            mask = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.circle(mask, (255, 255, 255, 255), (cx, cy), radius)

            masked_under = under.copy()
            masked_under.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            surface.blit(masked_under, (0, 0))

        elif self.mode is CircleWipeMode.CLOSE:
            radius = int((1.0 - t) * max_radius)  # max -> 0
            base = new_surface                    # 円の外側
            under = old_surface                   # 円の内側（戻り先）

            # 外側
            surface.blit(base, (0, 0))

            # 内側（円形マスク）
            mask = pygame.Surface((w, h), pygame.SRCALPHA)
            pygame.draw.circle(mask, (255, 255, 255, 255), (cx, cy), radius)

            masked_under = under.copy()
            masked_under.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            surface.blit(masked_under, (0, 0))
            return

        elif self.mode is CircleWipeMode.CLOSE_OPEN:
            if t < 0.5:
                # CLOSE パート（old -> 暗転）
                local = t / 0.5                         # 0 -> 1
                radius = int((1.0 - local) * max_radius)  # max -> 0

                # まず暗転色で塗る
                surface.fill(self.bg_color)

                # 中央だけ old_surface を残していく
                mask = pygame.Surface((w, h), pygame.SRCALPHA)
                pygame.draw.circle(mask, (255, 255, 255, 255), (cx, cy), radius)

                masked_old = old_surface.copy()
                masked_old.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                surface.blit(masked_old, (0, 0))
            else:
                # OPEN パート（暗転 -> new）
                local = (t - 0.5) / 0.5          # 0 -> 1
                radius = int(local * max_radius)

                # まず暗転色で塗る
                surface.fill(self.bg_color)

                # 円の内側に new_surface を表示
                mask = pygame.Surface((w, h), pygame.SRCALPHA)
                pygame.draw.circle(mask, (255, 255, 255, 255), (cx, cy), radius)

                masked_new = new_surface.copy()
                masked_new.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
                surface.blit(masked_new, (0, 0))
