import pygame
from typing import Any

class food(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill((255,10,0))
        self.rect = self.image.get_rect()
        self.rect.x = 550
        self.rect.y = 350