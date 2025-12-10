import pygame
from scripts.transition import Transition


class RotateWipeDirection:
    """
    回転ワイプの方向
    """
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"


class RotateWipeTransition(Transition):
    """
    回転ワイプトランジション

    Args:
        duration (float): トランジションの継続時間（秒）
        direction (RotateWipeDirection): ワイプの方向
        start_angle (float): 開始時の回転角度（度）
    """
    def __init__(self, duration=0.8, direction=RotateWipeDirection.LEFT, start_angle=90):
        super().__init__(duration)
        self.direction = direction
        self.start_angle = start_angle

    def render(self, surface, old_surface, new_surface):
        t = self.elapsed / self.duration
        t = max(0.0, min(1.0, t))

        w, h = surface.get_size()

        # まず old をそのまま描画
        surface.blit(old_surface, (0, 0))

        # 回転角: start_angle -> 0
        angle = self.start_angle * (1.0 - t)
        rotated = pygame.transform.rotate(new_surface, angle)
        rw, rh = rotated.get_size()

        # new の中心位置を決める（スライドイン）
        cx = w // 2
        cy = h // 2

        # 画面外から中心へ移動するオフセットを決める
        if self.direction == RotateWipeDirection.LEFT:
            # 右側から左へ
            start_dx = w  # 画面1個分右から
            dx = int(start_dx * (1.0 - t))
            dy = 0
        elif self.direction == RotateWipeDirection.RIGHT:
            start_dx = -w
            dx = int(start_dx * (1.0 - t))
            dy = 0
        elif self.direction == RotateWipeDirection.UP:
            start_dy = h
            dy = int(start_dy * (1.0 - t))
            dx = 0
        elif self.direction == RotateWipeDirection.DOWN:
            start_dy = -h
            dy = int(start_dy * (1.0 - t))
            dx = 0
        else:
            dx = dy = 0

        # 回転後の surface の中心を (cx+dx, cy+dy) に合わせる
        rect = rotated.get_rect(center=(cx + dx, cy + dy))
        surface.blit(rotated, rect.topleft)
