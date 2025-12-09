import pygame
from enum import Enum
from scripts.transition.base import Transition


class FadeMode(Enum):
    """
    フェードモード列挙型
    
    OUT   : フェードアウト
    IN    : フェードイン
    INOUT : フェードインアウト
    CROSS : クロスフェード
    """
    
    OUT = "out"
    IN = "in"
    INOUT = "inout"
    CROSS = "cross"


class FadeTransition(Transition):
    """
    フェード遷移クラス

    Args:
        duration (float): 遷移時間（秒）
        mode (FadeMode): フェードモード  
        color (tuple): フェードカラー（RGB）
    """

    def __init__(self, duration=0.5, mode=FadeMode.OUT, color=(0, 0, 0)):
        super().__init__(duration)

        self.mode = mode
        self.color = color

    def render(self, surface, old_surface, new_surface):
        t = self.elapsed / self.duration  # 0.0 → 1.0
        t = max(0.0, min(1.0, t))

        # クロスフェード 
        if self.mode == FadeMode.CROSS:
            alpha_new = int(t * 255)
            alpha_old = 255 - alpha_new

            temp_old = old_surface.copy()
            temp_new = new_surface.copy()

            temp_old.set_alpha(alpha_old)
            temp_new.set_alpha(alpha_new)

            surface.blit(temp_old, (0, 0))
            surface.blit(temp_new, (0, 0))
            return

        # フェードイン
        if self.mode == FadeMode.IN:
            # 先に new を描く
            surface.blit(new_surface, (0, 0))

            # 上からカラーをだんだん薄くしていく（t=0で真っ黒, t=1で透明）
            w, h = surface.get_size()
            rect_surf = pygame.Surface((w, h))
            rect_surf.fill(self.color)
            alpha = int((1.0 - t) * 255)
            rect_surf.set_alpha(alpha)
            surface.blit(rect_surf, (0, 0))
            return

        # フェードアウト
        if self.mode == FadeMode.OUT:
            surface.blit(old_surface, (0, 0))

            w, h = surface.get_size()
            rect_surf = pygame.Surface((w, h))
            rect_surf.fill(self.color)
            alpha = int(t * 255)
            rect_surf.set_alpha(alpha)
            surface.blit(rect_surf, (0, 0))
            return

        # フェードイン -> フェードアウト
        if self.mode == FadeMode.INOUT:
            w, h = surface.get_size()
            rect_surf = pygame.Surface((w, h))
            rect_surf.fill(self.color)

            if t < 0.5:
                # old をカラーにフェードアウト
                local_t = t / 0.5  # 0 → 1
                surface.blit(old_surface, (0, 0))
                alpha = int(local_t * 255)
                rect_surf.set_alpha(alpha)
                surface.blit(rect_surf, (0, 0))
            else:
                # カラーから new をフェードイン
                local_t = (t - 0.5) / 0.5  # 0 → 1
                surface.blit(new_surface, (0, 0))
                alpha = int((1.0 - local_t) * 255)
                rect_surf.set_alpha(alpha)
                surface.blit(rect_surf, (0, 0))
            return
