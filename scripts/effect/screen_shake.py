# scripts/effect/screen_shake.py
import math
import random
import pygame


class ScreenShakeEffect:
    """
    画面シェイクエフェクト

    Args:
        duration (float): シェイクの継続時間（秒）
        amplitude (float): シェイクの最大振幅（ピクセル）
        decay (bool): シェイクの減衰を有効にするかどう
        bg_color (tuple|None): シェイク中の背景色。Noneなら元の画面を使う
    """

    def __init__(
        self,
        duration: float = 0.4,
        amplitude: float = 16.0,
        decay: bool = True,
        bg_color=None,
    ):
        self.duration = duration
        self.amplitude = amplitude
        self.decay = decay
        self.bg_color = bg_color

        # 状態
        self.elapsed = 0.0
        self.active = False    # ← 実行中フラグ
        self.finished = False

    def start(self):
        """シェイクを開始する。何度でも呼べる。"""
        self.elapsed = 0.0
        self.active = True
        self.finished = False

    def stop(self):
        """強制停止"""
        self.active = False
        self.finished = True

    def reset(self):
        """start と同じだが名前で用途を分けたい場合に使う"""
        self.start()

    def update(self, dt: float):
        if not self.active or self.finished:
            return

        self.elapsed += dt
        if self.elapsed >= self.duration:
            self.elapsed = self.duration
            self.finished = True
            self.active = False

    @property
    def is_finished(self) -> bool:
        return self.finished

    def _apply(self, src: pygame.Surface, dst: pygame.Surface):
        if not self.active:
            # シェイクしてないならそのまま描画
            dst.blit(src, (0, 0))
            return

        t = self.elapsed / self.duration
        t = max(0.0, min(1.0, t))

        # 揺れの減衰
        strength = 1.0 - t if self.decay else 1.0
        amp = self.amplitude * strength

        # ランダム方向
        theta = random.random() * math.tau
        dx = int(math.cos(theta) * amp)
        dy = int(math.sin(theta) * amp)

        # 背景色が指定されていれば塗る
        if self.bg_color is not None:
            dst.fill(self.bg_color)

        # シェイクされた描画
        dst.blit(src, (dx, dy))

    def apply(self, surface: pygame.Surface):
        # 元の絵をコピーしてから apply に渡す
        temp = surface.copy()
        self._apply(temp, surface)
