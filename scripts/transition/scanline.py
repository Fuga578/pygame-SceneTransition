import pygame
from enum import Enum, auto
from scripts.transition import Transition


class ScanlineDirection(Enum):
    """
    交互スキャンラインの抜け方向

    VERTICAL : 横帯が交互に左右へ抜ける
    HORIZONTAL    : 縦帯が交互に上下へ抜ける
    """
    VERTICAL = auto()
    HORIZONTAL = auto()


def _ease_in_out(t: float) -> float:
    # 好みで。不要なら return t にしてOK
    # return t * t * (3.0 - 2.0 * t)
    return t


class ScanlineTransition(Transition):
    """
    FRLGエンカウント風：
    old_surface を帯に分割し、交互に左右/上下へスライドアウトして new_surface を露出させる

    Args:
        duration (float): 遷移時間（秒）
        direction (ScanlineDirection): 抜け方向（LEFT/RIGHT/UP/DOWN）
        band_thickness (int): 帯の太さ（px）
        gap (int): 帯の隙間（px）
        easing (bool): Trueならイージング
        swap (bool): Trueなら交互パターンを反転（偶数/奇数の向きを入れ替え）
    """
    def __init__(
        self,
        duration: float = 0.45,
        direction: ScanlineDirection = ScanlineDirection.VERTICAL,
        band_thickness: int = 6,
        gap: int = 0,
        easing: bool = True,
        swap: bool = False,
    ):
        super().__init__(duration)
        self.direction = direction
        self.band_thickness = max(1, band_thickness)
        self.gap = max(0, gap)
        self.easing = easing
        self.swap = swap

    def render(self, surface, old_surface, new_surface):
        t = 0.0 if self.duration <= 0 else self.elapsed / self.duration
        t = max(0.0, min(1.0, t))
        if self.easing:
            t = _ease_in_out(t)

        w, h = surface.get_size()
        pitch = self.band_thickness + self.gap

        # new を全面に敷く（old が抜けた部分から見える）
        surface.blit(new_surface, (0, 0))

        # 抜け量（0 -> 画面外へ）
        off_x = int(t * w)
        off_y = int(t * h)

        if self.direction == ScanlineDirection.VERTICAL:
            for y in range(0, h, pitch):
                band_h = min(self.band_thickness, h - y)
                rect = pygame.Rect(0, y, w, band_h)

                band_index = y // pitch
                even = (band_index % 2 == 0)
                if self.swap:
                    even = not even
                dx = (-off_x if even else off_x)

                surface.blit(old_surface, (dx, y), rect)

        else:
            for x in range(0, w, pitch):
                band_w = min(self.band_thickness, w - x)
                rect = pygame.Rect(x, 0, band_w, h)

                band_index = x // pitch
                even = (band_index % 2 == 0)
                if self.swap:
                    even = not even
                dy = (-off_y if even else off_y)

                surface.blit(old_surface, (x, dy), rect)
