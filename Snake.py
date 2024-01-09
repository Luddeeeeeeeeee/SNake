import pygame
from Player import player

pygame.init()
class Game:
    def __init__(self):
        player_sprite = player()
        self.player = pygame.sprite.GroupSingle(player_sprite)
    def run(self):
        self.player.draw(screen)


Clock = pygame.time.Clock()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number))

run = True

game = Game()

while run:
    
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,0))
    game.run()
    pygame.display.flip()
    Clock.tick(60)