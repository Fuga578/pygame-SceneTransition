import random
import pygame
from scripts.transition import Transition


class PuzzleTransition(Transition):
    """
    パズル遷移クラス

    Args:
        duration (float): 遷移時間（秒）
        cols (int): タイルの列数
        rows (int): タイルの行数
        seed (int | None): タイルのめくる順番を決めるシード値（None の場合ランダム）
    """
    def __init__(self, duration=0.8, cols=8, rows=6, seed=None):
        super().__init__(duration)
        self.cols = max(1, cols)
        self.rows = max(1, rows)
        self.seed = seed

        self._order = None  # タイルをめくる順番（インデックスのリスト）

    def start(self):
        super().start()
        # タイル順を初期化
        indices = list(range(self.cols * self.rows))
        rnd = random.Random(self.seed)
        rnd.shuffle(indices)
        self._order = indices

    def render(self, surface, old_surface, new_surface):
        t = self.elapsed / self.duration
        t = max(0.0, min(1.0, t))

        w, h = surface.get_size()
        tile_w = w // self.cols
        tile_h = h // self.rows
        total_tiles = self.cols * self.rows

        # 今の t で何枚めくるか
        visible_tiles = int(total_tiles * t)

        # まず old を全画面に表示
        surface.blit(old_surface, (0, 0))

        if self._order is None:
            return

        for n in range(visible_tiles):
            idx = self._order[n]
            cx = idx % self.cols
            cy = idx // self.cols

            src_rect = pygame.Rect(cx * tile_w, cy * tile_h, tile_w, tile_h)
            surface.blit(new_surface, src_rect.topleft, src_rect)
