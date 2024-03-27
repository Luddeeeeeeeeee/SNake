import pygame
from Player import player_head
from Player import player_body
from FOOD import food
import random

pygame.init()
class Game:

    def __init__(self):
        self.dircetion = "RIGHT"
        self.player_sprite = player_head()
        self.food_sprite = food()
        self.player_head = pygame.sprite.GroupSingle(self.player_sprite)
        self.food = pygame.sprite.GroupSingle(self.food_sprite)
        self.x = 350
        self.y = 350
        self.player_segment = []
        self.amount_of_segmetnts = 1
        self.my_font = pygame.font.Font("freesansbold.ttf", 39)
        
    def drawing_player(self):
        for segment in self.player_segment:
            screen.blit(segment.image, segment.rect)

    def uppdate_player(self):
        global brun 

        self.player_head.sprite.move(self.dircetion)
        if self.player_head.sprite.rect.x >= 800 or self.player_head.sprite.rect.x <= 0:
            brun = False
            self.player_head.sprite.rect.x = 350
            self.player_head.sprite.rect.y = 350
            self.food.sprite.rect.x = 550
            self.food.sprite.rect.y = 350
            self.amount_of_segmetnts = 1
            self.x = 350
            self.y = 350
            self.dircetion = "RIGHT"
            self.player_segment.clear()


        if self.player_head.sprite.rect.y >= 800 or self.player_head.sprite.rect.y <= 0:
            brun = False
            self.player_head.sprite.rect.x = 350
            self.player_head.sprite.rect.y = 350
            self.food.sprite.rect.x = 550
            self.food.sprite.rect.y = 350
            self.amount_of_segmetnts = 1
            self.x = 350
            self.y = 350
            self.dircetion = "RIGHT"
            self.player_segment.clear()


        for segment in self.player_segment:
            if self.player_head.sprite.rect.colliderect(segment.rect):
                brun = False
                self.player_head.sprite.rect.x = 350
                self.player_head.sprite.rect.y = 350
                self.food.sprite.rect.x = 550
                self.food.sprite.rect.y = 350
                self.amount_of_segmetnts = 1
                self.x = 350
                self.y = 350
                self.dircetion = "RIGHT"
                self.player_segment.clear()
        
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

        if len(self.player_segment) > self.amount_of_segmetnts:
            self.player_segment.pop(0)
        
        

    def food_collison(self):
        if pygame.sprite.spritecollide(self.player_head.sprite,self.food,False):
            self.food.sprite.rect.x = random.randint(40,740)
            self.food.sprite.rect.y = random.randint(40,740)
            self.amount_of_segmetnts += 1
    def start_screen(self):
        text = self.my_font.render("Press Space to start", False, (255, 255, 255))
        screen.blit(text, (150,350))


    def run(self):
        self.player_head.draw(screen)
        self.food.draw(screen)
        self.food_collison()
        self.uppdate_player()
        self.drawing_player()




Clock = pygame.time.Clock()
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_size * cell_number,cell_size * cell_number))

run = True

game = Game()
brun = False
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

            if event.key == pygame.K_SPACE:
                brun = True
                
    screen.fill((0,0,0))
    game.start_screen()
    if brun == True:

        screen.fill((0,0,0))
        game.run()
    
    pygame.display.flip()
    Clock.tick(7) 