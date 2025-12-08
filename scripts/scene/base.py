import pygame
from abc import ABC, abstractmethod


class Scene(ABC):

    @abstractmethod
    def handle(self):
        """入力処理を行います。"""
        pass

    @abstractmethod
    def update(self, dt: float):
        """状態更新を行います。"""
        pass

    @abstractmethod
    def render(self, surface: pygame.Surface):
        """描画を行います。"""
        pass