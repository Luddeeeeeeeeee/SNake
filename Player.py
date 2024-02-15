from typing import Any
import pygame


class player_head(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill((100,100,0))
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 350

    def move(self,dircetion) -> None:
        if dircetion == "RIGHT":
            self.rect.x += 40
        if dircetion == "UP":
            self.rect.y -= 40
        if dircetion == "DOWN":
            self.rect.y += 40
        if dircetion == "LEFT":
            self.rect.x -= 40

class player_body(pygame.sprite.Sprite):
    def __init__(self,x,y) -> None:
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill((0,100,0))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x




                
                


            
                

