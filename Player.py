from typing import Any
import pygame


class player(pygame.sprite.Sprite):
    def __init__(self,x) -> None:
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill((0,100,0))
        self.rect = self.image.get_rect()
        self.rect = x,350
        
        