import pygame
from Player import player_head
from Player import player_body
from FOOD import food

pygame.init()
class Game:

    def __init__(self):
        self.dircetion = "RIGHT"
        self.player_sprite = player_head()
        self.food_sprite = food()
        self.player_head = pygame.sprite.GroupSingle(self.player_sprite)
        self.food = pygame.sprite.Group(self.food_sprite)
        self.x = 350
        self.y = 350
        self.player_segment = []
        
    def drawing_player(self):
        for segment in self.player_segment:
            screen.blit(segment.image, segment.rect)

    def uppdate_player(self):

        self.player_head.sprite.move(self.dircetion)
        for segment in self.player_segment:
            if self.player_head.sprite.rect.colliderect(segment.rect):
                print("Game Over")
        
        if self.player_head.sprite.rect.x == self.x + 40 and self.dircetion == "RIGHT":
            self.player_segment.append(player_body(self.x,self.y))
            self.x = self.player_head.sprite.rect.x

        if self.player_head.sprite.rect.y == self.y + 40 and self.dircetion == "DOWN":
            self.player_segment.append(player_body(self.x,self.y))
            self.y = self.player_head.sprite.rect.y

        if self.player_head.sprite.rect.x == self.x - 40 and self.dircetion == "LEFT":
            self.player_segment.append(player_body(self.x,self.y))
            self.x = self.player_head.sprite.rect.x

        if self.player_head.sprite.rect.y == self.y - 40 and self.dircetion == "UP":
            self.player_segment.append(player_body(self.x,self.y))
            self.y = self.player_head.sprite.rect.y

        if len(self.player_segment) > 3:
            self.player_segment.pop(0)
    def run(self):
        self.player_head.draw(screen)
        self.food.draw(screen)
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

            if event.key == pygame.K_s:
                game.dircetion = "DOWN"

            if event.key == pygame.K_d:
                game.dircetion = "RIGHT"
                

            if event.key == pygame.K_a:
                game.dircetion = "LEFT"
                
    screen.fill((0,0,0))
    game.run()
    pygame.display.flip()
    Clock.tick(8) 