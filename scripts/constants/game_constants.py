from scripts.constants.meta import ConstantMeta


class GameConstants(metaclass=ConstantMeta):
    
    # ゲーム画面幅
    SCREEN_WIDTH = 800

    # ゲーム画面高さ
    SCREEN_HEIGHT = 600
    
    # フレームレート
    FPS = 60

    # 色
    COLORS = {
        "black": (0, 0, 0),
        "white": (255, 255, 255),
    }
