import pygame
from Player import player

pygame.init()
class Game:

    def __init__(self):

        self.player_sprite = player(350)
        self.player = pygame.sprite.Group(self.player_sprite)
        self.amount = 3
    def drawing_player(self):
        x = 350
        for t in range(self.amount):
            x -= 40
            player_sprite = player(x)
            self.player.add(player_sprite)


    def run(self):
        self.drawing_player()
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