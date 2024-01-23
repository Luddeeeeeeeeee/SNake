import pygame
from Player import player

pygame.init()
class Game:

    def __init__(self):
        self.dircetion = "RIGHT"
        self.where_to_turn_x = None
        self.where_to_turn_y = None
        self.player_sprite = player(350,(2),)
        self.player_head = pygame.sprite.GroupSingle(self.player_sprite)
        self.player_body = pygame.sprite.Group()
        self.amount = 2
        self.g = 2

    def drawing_player(self):
        x = self.player_head.sprite.rect.x - 40
        t = 0
        
        if self.g >= 0:
            for t in range(self.amount):
                player_sprite = player(x,(1),)
                self.player_body.add(player_sprite)
                x = self.player_body.sprites()[t].rect.x - 40
                t += 1
                self.g -= 1

    def uppdate_player(self):
        self.player_head.sprite.move(self.dircetion)
    def run(self):

        
        self.player_head.draw(screen)
        self.player_body.draw(screen)
        self.player_body.update(self.where_to_turn_x,self.where_to_turn_y)
        self.uppdate_player()
        self.drawing_player()



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

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                game.dircetion = "UP"
                game.where_to_turn_x = game.player_head.sprite.rect.x

            if event.key == pygame.K_s:
                game.dircetion = "DOWN"
                game.where_to_turn_x = game.player_head.sprite.rect.x

            if event.key == pygame.K_d:
                game.dircetion = "RIGHT"
                game.where_to_turn_y = game.player_head.sprite.rect.y

            if event.key == pygame.K_a:
                game.dircetion = "LEFT"
                game.where_to_turn_y = game.player_head.sprite.rect.y
                
    screen.fill((0,0,0))
    game.run()
    pygame.display.flip()
    Clock.tick(11) 