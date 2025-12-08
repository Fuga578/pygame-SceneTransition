class ConstantMeta(type):
    def __setattr__(cls, name, value):
        """定数の追加・上書きを禁止します。"""
        if name in cls.__dict__:
            raise AttributeError(f"定数 '{name}' は上書きできません。")
        raise AttributeError(f"定数 '{name}' は追加できません。")

    def __call__(cls, *args, **kwargs):
        """クラスのインスタンス化を禁止します。"""
        raise TypeError(f"{cls.__name__} はインスタンス化できません。")