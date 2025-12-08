import sys
import pygame
from scripts.constants.game_constants import GameConstants
from scripts.scene.manager import SceneManager
from scripts.scene.ids import SceneID


class Game:

    def __init__(self):
        pygame.init()

        # ウィンドウの設定
        self.screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
        
        # FPSの設定
        self.clock = pygame.time.Clock()

        # 入力
        self.inputs = {
            "enter": False,
            "w": False,
        }

        # シーン
        self.scene_manager = SceneManager(self, SceneID.TITLE)

    def exit(self):
        pygame.quit()
        sys.exit()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.exit()
                if event.key == pygame.K_RETURN:
                    self.inputs["enter"] = True
                if event.key == pygame.K_w:
                    self.inputs["w"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    self.inputs["enter"] = False
                if event.key == pygame.K_w:
                    self.inputs["w"] = False

    def run(self):
        while True:

            # デルタタイム
            dt = self.clock.tick(GameConstants.FPS) / 1000.0

            # 背景の塗りつぶし
            self.screen.fill(GameConstants.COLOR["white"])

            # シーンの更新と描画
            self.scene_manager.handle()
            self.scene_manager.update(dt)
            self.scene_manager.render(self.screen)

            # イベント処理
            self.handle_events()

            # 画面更新
            pygame.display.update()
