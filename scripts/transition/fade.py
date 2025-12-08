import pygame
from scripts.transition.base import Transition


class FadeTransition(Transition):
    def __init__(self, duration=0.5, mode="black"):
        """
        mode: "black" or "white" or "cross"
        """
        super().__init__(duration)
        self.mode = mode

    def render(self, surface, old_surface, new_surface):
        dt = self.elapsed / self.duration  # 0.0 → 1.0

        # クロスフェード
        if self.mode == "cross":
            alpha_new = int(dt * 255)
            alpha_old = 255 - alpha_new

            temp_old = old_surface.copy()
            temp_new = new_surface.copy()

            temp_old.set_alpha(alpha_old)
            temp_new.set_alpha(alpha_new)

            surface.blit(temp_old, (0, 0))
            surface.blit(temp_new, (0, 0))

        else:
            # 古い画面を描画
            surface.blit(old_surface, (0, 0))

            # 黒 or 白の板でフェード
            if self.mode == "black":
                color = (0, 0, 0)
            else:
                color = (255, 255, 255)

            w, h = surface.get_size()
            rect_surf = pygame.Surface((w, h))
            rect_surf.fill(color)
            rect_surf.set_alpha(int(dt * 255))

            surface.blit(rect_surf, (0, 0))
