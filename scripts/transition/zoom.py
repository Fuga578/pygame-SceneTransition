import pygame
from enum import Enum
from scripts.transition import Transition


class ZoomMode(Enum):
    IN = "in"      # new をズームインさせて登場
    OUT = "out"    # old をズームアウトさせて退場
    INOUT = "inout"  # （お好みで）old縮小->new拡大 みたいな複合もできる


class ZoomTransition(Transition):
    """
    ズームトランジション

    Args:
        duration (float): 遷移時間（秒）
        mode (ZoomMode): ズームモード
        min_scale (float): 最小スケール（OUTやINOUTでどこまで縮めるか）
        max_scale (float): 最大スケール（INでどこから拡大してくるか）
        bg_color (tuple): INOUT のときに使う背景色
    """
    def __init__(
        self,
        duration: float = 0.7,
        mode: ZoomMode = ZoomMode.IN,
        min_scale: float = 0.01,
        max_scale: float = 2.0,
        bg_color=None,
    ):
        super().__init__(duration)
        self.mode = mode
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.bg_color = bg_color or (0, 0, 0)

    def render(self, surface, old_surface, new_surface):
        t = max(0.0, min(1.0, self.elapsed / self.duration))
        w, h = surface.get_size()
        cx, cy = w // 2, h // 2

        # --- IN: new がズームインして登場 ---
        if self.mode is ZoomMode.IN:
            surface.blit(old_surface, (0, 0))

            scale = self.max_scale - (self.max_scale - 1.0) * t  # max -> 1.0
            zw, zh = max(1, int(w * scale)), max(1, int(h * scale))
            zoomed = pygame.transform.smoothscale(new_surface, (zw, zh))
            rect = zoomed.get_rect(center=(cx, cy))
            surface.blit(zoomed, rect.topleft)

        # --- OUT: old がズームアウトして退場 ---
        elif self.mode is ZoomMode.OUT:
            surface.blit(new_surface, (0, 0))

            scale = 1.0 - (1.0 - self.min_scale) * t  # 1.0 -> min_scale
            zw, zh = max(1, int(w * scale)), max(1, int(h * scale))
            zoomed = pygame.transform.smoothscale(old_surface, (zw, zh))
            rect = zoomed.get_rect(center=(cx, cy))
            surface.blit(zoomed, rect.topleft)

        # --- INOUT: old縮小 -> new拡大（背景は bg_color） ---
        elif self.mode is ZoomMode.INOUT:
            if t < 0.5:
                # 前半: old を縮小して消える
                local = t / 0.5  # 0 → 1

                scale = 1.0 - (1.0 - self.min_scale) * local  # 1.0 -> min_scale
                zw, zh = max(1, int(w * scale)), max(1, int(h * scale))
                zoomed = pygame.transform.smoothscale(old_surface, (zw, zh))
                rect = zoomed.get_rect(center=(cx, cy))

                # 背景は old/new ではなく、常に bg_color
                surface.fill(self.bg_color)
                surface.blit(zoomed, rect.topleft)

            else:
                # 後半: new を拡大して現れる
                local = (t - 0.5) / 0.5  # 0 → 1

                scale = self.min_scale + (1.0 - self.min_scale) * local  # min_scale -> 1.0
                zw, zh = max(1, int(w * scale)), max(1, int(h * scale))
                zoomed = pygame.transform.smoothscale(new_surface, (zw, zh))
                rect = zoomed.get_rect(center=(cx, cy))

                surface.fill(self.bg_color)
                surface.blit(zoomed, rect.topleft)
                