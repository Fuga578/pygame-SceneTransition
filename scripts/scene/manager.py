import pygame
from scripts.scene.ids import SceneID, Scene, TitleScene, FadeScene


class SceneManager:
    """
    シーン管理クラス
    
    Args:
        game (Game): ゲーム本体のインスタンス
        start_scene_id (SceneID): 最初に表示するシーンのID
    """
    def __init__(self, game, start_scene_id: SceneID):
        self.game = game
        self.current_scene: Scene = self._create_scene(start_scene_id)

        # トランジション関連
        self.transition = None      # 現在のトランジション（なければ None）
        self._next_scene = None     # トランジション後に切り替えるシーン
        self._old_surface = None    # トランジション用の古い画面キャプチャ
        self._new_surface = None    # トランジション用の新しい画面キャプチャ

    def _create_scene(self, scene_id: SceneID) -> Scene:
        if scene_id == SceneID.TITLE:
            return TitleScene(self.game, self)
        elif scene_id == SceneID.FADE:
            return FadeScene(self.game, self)
        else:
            raise ValueError(f"未知の SceneID: {scene_id}")

    def change_scene(self, scene_id: SceneID, transition=None):
        # トランジション無しの場合、即切り替え
        if transition is None:
            self.current_scene = self._create_scene(scene_id)
            return

        # 次のシーンを先に作っておく
        self._next_scene = self._create_scene(scene_id)
        self.transition = transition

        # 画面キャプチャ用 Surface 用意
        screen = pygame.display.get_surface()
        w, h = screen.get_size()
        self._old_surface = pygame.Surface((w, h))
        self._new_surface = pygame.Surface((w, h))

        # 現在シーンを old_surface に描画して保存
        self._old_surface.fill((0, 0, 0))
        self.current_scene.render(self._old_surface)

        # トランジション開始
        self.transition.start()

    def handle(self):
        # トランジション中は入力を受け付けない
        if self.transition is None:
            self.current_scene.handle()

    def update(self, dt: float):
        # 遷移中の場合
        if self.transition:
            # self._next_scene.update(dt)   # 遷移中に新しいシーンも動かしたければコメントを外す
            
            # 遷移が完了した場合、次のシーンに切り替え
            is_finished = self.transition.update(dt)
            if is_finished:
                self.current_scene = self._next_scene
                self._next_scene = None
                self.transition = None
        else:
            self.current_scene.update(dt)

    def render(self, surface):
        if self.transition:
            # 新しいシーンを new_surface に描画
            self._new_surface.fill((0, 0, 0))
            self._next_scene.render(self._new_surface)

            # トランジション描画
            self.transition.render(
                surface,
                self._old_surface,
                self._new_surface
            )
        else:
            self.current_scene.render(surface)
