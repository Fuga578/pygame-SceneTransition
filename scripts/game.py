import sys
import pygame
from scripts.constants import GameConstants
from scripts.scene.ids import SceneID
from scripts.scene.manager import SceneManager


class Game:

    def __init__(self):
        pygame.init()

        # ウィンドウの設定
        self.screen = pygame.display.set_mode((GameConstants.SCREEN_WIDTH, GameConstants.SCREEN_HEIGHT))
        
        # FPSの設定
        self.clock = pygame.time.Clock()

        # 入力
        self.inputs = {
            "esc": False,
            "enter": False,
            "w": False,
            "a": False,
            "s": False,
            "d": False,
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "p": False,
            "q": False,
            "z": False,
            "x": False,
            "c": False,
            "v": False,
            "b": False,
            "n": False,
            "m": False,
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
                    self.inputs["esc"] = True
                if event.key == pygame.K_RETURN:
                    self.inputs["enter"] = True
                if event.key == pygame.K_w:
                    self.inputs["w"] = True
                if event.key == pygame.K_a:
                    self.inputs["a"] = True
                if event.key == pygame.K_s:
                    self.inputs["s"] = True
                if event.key == pygame.K_d:
                    self.inputs["d"] = True
                if event.key == pygame.K_UP:
                    self.inputs["up"] = True
                if event.key == pygame.K_DOWN:
                    self.inputs["down"] = True
                if event.key == pygame.K_LEFT:
                    self.inputs["left"] = True
                if event.key == pygame.K_RIGHT:
                    self.inputs["right"] = True
                if event.key == pygame.K_p:
                    self.inputs["p"] = True
                if event.key == pygame.K_q:
                    self.inputs["q"] = True
                if event.key == pygame.K_z:
                    self.inputs["z"] = True
                if event.key == pygame.K_x:
                    self.inputs["x"] = True
                if event.key == pygame.K_c:
                    self.inputs["c"] = True
                if event.key == pygame.K_v:
                    self.inputs["v"] = True
                if event.key == pygame.K_b:
                    self.inputs["b"] = True
                if event.key == pygame.K_n:
                    self.inputs["n"] = True
                if event.key == pygame.K_m:
                    self.inputs["m"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.inputs["esc"] = False
                if event.key == pygame.K_RETURN:
                    self.inputs["enter"] = False
                if event.key == pygame.K_w:
                    self.inputs["w"] = False
                if event.key == pygame.K_a:
                    self.inputs["a"] = False
                if event.key == pygame.K_s:
                    self.inputs["s"] = False
                if event.key == pygame.K_d:
                    self.inputs["d"] = False
                if event.key == pygame.K_UP:
                    self.inputs["up"] = False
                if event.key == pygame.K_DOWN:
                    self.inputs["down"] = False
                if event.key == pygame.K_LEFT:
                    self.inputs["left"] = False
                if event.key == pygame.K_RIGHT:
                    self.inputs["right"] = False
                if event.key == pygame.K_p:
                    self.inputs["p"] = False
                if event.key == pygame.K_q:
                    self.inputs["q"] = False
                if event.key == pygame.K_z:
                    self.inputs["z"] = False
                if event.key == pygame.K_x:
                    self.inputs["x"] = False
                if event.key == pygame.K_c:
                    self.inputs["c"] = False
                if event.key == pygame.K_v:
                    self.inputs["v"] = False
                if event.key == pygame.K_b:
                    self.inputs["b"] = False
                if event.key == pygame.K_n:
                    self.inputs["n"] = False
                if event.key == pygame.K_m:
                    self.inputs["m"] = False

    def run(self):
        while True:

            # デルタタイム
            dt = self.clock.tick(GameConstants.FPS) / 1000.0

            # 背景の塗りつぶし
            self.screen.fill(GameConstants.COLORS["white"])

            # シーンの更新と描画
            self.scene_manager.handle()
            self.scene_manager.update(dt)
            self.scene_manager.render(self.screen)

            # イベント処理
            self.handle_events()

            # 画面更新
            pygame.display.update()
