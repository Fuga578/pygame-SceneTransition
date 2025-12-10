from enum import Enum, auto


class SceneID(Enum):
    TITLE = auto()  # タイトル画面
    FADE = auto()   # フェード遷移デモシーン
    SLIDE = auto()  # スライド遷移デモシーン
    WIPE = auto()   # ワイプ遷移デモシーン
    BLIND = auto()   # ブラインド遷移デモシーン
    CIRCLE_WIPE = auto()    # 円形ワイプ遷移デモシーン
    PUZZLE = auto()  # パズル遷移デモシーン
    ROTATE_WIPE = auto()  # 回転ワイプ遷移デモシーン