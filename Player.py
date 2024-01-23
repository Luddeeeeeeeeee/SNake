from typing import Any
import pygame


class player(pygame.sprite.Sprite):
    def __init__(self,x,b_or_h,) -> None:
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill((0,100,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 350
        self.b_or_h = b_or_h

        
        
    def move(self,dircetion) -> None:
        if dircetion == "RIGHT":
            self.rect.x += 10
        if dircetion == "UP":
            self.rect.y -= 10
        if dircetion == "DOWN":
            self.rect.y += 10
        if dircetion == "LEFT":
            self.rect.x -= 10


    def update(self,where_to_turn_x,where_to_turn_y) -> None:
        if self.b_or_h == 1:
            
            
            if self.rect.x == where_to_turn_x:
                self.rect.y -= 10
            if self.rect.y == where_to_turn_y:
                self.rect.x += 10

            else:
                self.rect.x += 10

