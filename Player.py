from typing import Any
import pygame
from pygame.math import Vector2

class player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill((0,100,0))
        self.body = [Vector2(10,10)]
        self.rect = self.rect
        

    def update(self) -> None:
        for block in self.body:
            x_pos = int(block.x * 40)
            y_pos = int(block.y * 40)
            block_rect = pygame.Rect(x_pos,y_pos,self.image)
            self.Rect = block_rect
            

        