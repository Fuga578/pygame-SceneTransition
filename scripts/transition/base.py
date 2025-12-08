from abc import ABC, abstractmethod


class Transition(ABC):
    def __init__(self, duration=0.5):
        self.duration = duration
        self.elapsed = 0.0
        self.active = False

    def start(self):
        self.elapsed = 0.0
        self.active = True

    def update(self, dt):
        # まだアクティブでなければ即終了
        if not self.active:
            return True
        
        self.elapsed += dt

        is_finished = False
        if self.elapsed >= self.duration:
            self.elapsed = self.duration
            self.active = False
            is_finished = True  # 終了判定
        
        return is_finished

    @abstractmethod
    def render(self, surface, old_surface, new_surface):
        pass
