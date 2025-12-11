import pygame
from enum import Enum
from scripts.transition import Transition


class MosaicMode(Enum):
    """
    モザイク遷移モード

    OUT   : old がモザイク化しつつ、new がフェードイン
    IN    : old の上に、モザイクな new がだんだんクリアになっていく
    INOUT : 前半 old がモザイク化し、後半 new のモザイクがクリアになっていく
    """
    OUT = "out"
    IN = "in"
    INOUT = "inout"


class MosaicTransition(Transition):
    """
    モザイクトランジション

    Args:
        duration     : 遷移時間（秒）
        mode         : MosaicMode
        min_block    : 最小ブロックサイズ（1 ならモザイク無しに近い）
        max_block    : 最大ブロックサイズ（大きいほど荒いモザイク）
    """

    def __init__(
        self,
        duration: float = 0.8,
        mode: MosaicMode = MosaicMode.OUT,
        min_block: int = 4,
        max_block: int = 40,
    ):
        super().__init__(duration)
        self.mode = mode
        self.min_block = max(1, min_block)
        self.max_block = max(self.min_block, max_block)

    # --------------------------------------------------------
    # 内部ヘルパー：モザイク化
    # --------------------------------------------------------
    def _pixelate(self, surface: pygame.Surface, block_size: int) -> pygame.Surface:
        """
        block_size を大きくすると荒いモザイクになる。
        """
        block_size = max(1, block_size)
        if block_size == 1:
            return surface.copy()

        w, h = surface.get_size()

        small_w = max(1, w // block_size)
        small_h = max(1, h // block_size)

        small = pygame.transform.smoothscale(surface, (small_w, small_h))
        mosaic = pygame.transform.scale(small, (w, h))
        return mosaic

    # --------------------------------------------------------
    # メイン描画
    # --------------------------------------------------------
    def render(self, surface, old_surface, new_surface):
        t = 0.0 if self.duration <= 0 else self.elapsed / self.duration
        t = max(0.0, min(1.0, t))
        w, h = surface.get_size()

        # -----------------------------
        # OUT: old がモザイク化しながら new に切り替え
        # -----------------------------
        if self.mode is MosaicMode.OUT:
            # 時間が進むほど old のモザイクが荒くなる
            block = int(self.min_block + (self.max_block - self.min_block) * t)
            block = max(1, block)

            mosaic_old = self._pixelate(old_surface, block)
            surface.blit(mosaic_old, (0, 0))

            # new をフェードイン
            alpha = int(t * 255)
            if alpha > 0:
                temp_new = new_surface.copy()
                temp_new.set_alpha(alpha)
                surface.blit(temp_new, (0, 0))

        # -----------------------------
        # IN: old の上にモザイクな new が出てきて、だんだんクリアに
        # -----------------------------
        elif self.mode is MosaicMode.IN:
            surface.blit(old_surface, (0, 0))

            # 時間が進むほど new のモザイクが細かくなる
            block = int(self.max_block - (self.max_block - self.min_block) * t)
            block = max(1, block)

            mosaic_new = self._pixelate(new_surface, block)

            alpha = int(t * 255)
            if alpha > 0:
                temp = mosaic_new.copy()
                temp.set_alpha(alpha)
                surface.blit(temp, (0, 0))

        # -----------------------------
        # INOUT:
        #   前半 : old がだんだんモザイク化（崩れていく）
        #   後半 : new がモザイク状態からだんだんクリアになる
        # -----------------------------
        elif self.mode is MosaicMode.INOUT:
            if t < 0.5:
                # 前半: old_surface がモザイクになっていく
                local = t / 0.5  # 0 → 1

                # clear → 粗いモザイクへ
                block = int(self.min_block + (self.max_block - self.min_block) * local)
                block = max(1, block)

                mosaic_old = self._pixelate(old_surface, block)
                surface.blit(mosaic_old, (0, 0))

            else:
                # 後半: モザイクな new_surface が徐々に明瞭化
                local = (t - 0.5) / 0.5  # 0 → 1

                # 粗いモザイク → 細かいモザイク（min_block=1 なら完全クリア）
                block = int(self.max_block - (self.max_block - self.min_block) * local)
                block = max(1, block)

                mosaic_new = self._pixelate(new_surface, block)
                surface.blit(mosaic_new, (0, 0))
