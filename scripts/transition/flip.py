import pygame
from enum import Enum
from scripts.transition import Transition


class FlipAxis(Enum):
    """
    フリップ軸

    Y: 左右方向に潰れて反転（Y軸回転っぽい）
    X: 上下方向に潰れて反転（X軸回転っぽい）
    """
    Y = "y"
    X = "x"


def _ease_in_out(t: float) -> float:
    # なめらかに（不要なら return t）
    return t * t * (3.0 - 2.0 * t)


class FlipTransition(Transition):
    """
    フリップトランジション（カード反転風）

    Args:
        duration (float): 遷移時間（秒）
        axis (FlipAxis): フリップ軸（X or Y）
        easing (bool): Trueならイージング
        min_scale (float): 0 に近いほど中央で細くなる（0は不可）
        bg_color (tuple): 背景色（RGBタプル）
    """
    def __init__(
        self,
        duration: float = 0.6,
        axis: FlipAxis = FlipAxis.Y,
        easing: bool = True,
        min_scale: float = 0.03,
        bg_color: tuple = (0, 0, 0)
    ):
        super().__init__(duration)
        self.axis = axis
        self.easing = easing
        self.min_scale = max(0.001, min_scale)
        self.bg_color = bg_color

    def render(self, surface, old_surface, new_surface):
        t = 0.0 if self.duration <= 0 else self.elapsed / self.duration
        t = max(0.0, min(1.0, t))
        if self.easing:
            t = _ease_in_out(t)

        w, h = surface.get_size()
        cx, cy = w // 2, h // 2

        # 0..0.5 は old、0.5..1 は new
        if t < 0.5:
            local = t / 0.5
            src = old_surface
            scale = 1.0 - (1.0 - self.min_scale) * local  # 1.0 -> min
        else:
            local = (t - 0.5) / 0.5
            src = new_surface
            scale = self.min_scale + (1.0 - self.min_scale) * local  # min -> 1.0

        # 軸で潰す方向を変える
        if self.axis is FlipAxis.Y:
            sw, sh = max(1, int(w * scale)), h
        else:
            sw, sh = w, max(1, int(h * scale))

        scaled = pygame.transform.smoothscale(src, (sw, sh))
        rect = scaled.get_rect(center=(cx, cy))

        surface.fill(self.bg_color)

        # フリップ本体（前半は old の縮小、後半は new の復帰）
        surface.blit(scaled, rect.topleft)

        # 立体感の簡易シャドウ（中央ほど暗く）
        # if self.shadow:
        #     k = 1.0 - scale
        #     alpha = int(min(180, max(0, k * 220)))
        #     if alpha > 0:
        #         shade = pygame.Surface((w, h), pygame.SRCALPHA)
        #         shade.fill((0, 0, 0, alpha))
        #         surface.blit(shade, (0, 0))
