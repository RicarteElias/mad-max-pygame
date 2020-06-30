import pygame, sys
from pygame.locals import *
import random, time

 
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 565
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Eu vivo eu morro \n eu vivo de novo", True, BLACK)
background = pygame.image.load("road.png")

DISPLAYSURF = pygame.display.set_mode((565,600))
pygame.display.set_caption("Game")
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)


class Tree(pygame.sprite.Sprite,):
      def __init__(self, obstacle):
        super().__init__() 
        self.image = pygame.image.load(obstacle)
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(420,SCREEN_WIDTH)
                                                 , 0))

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(400, SCREEN_WIDTH ), 0)

class Enemy(pygame.sprite.Sprite):
      def __init__(self,obstacle):
        super().__init__() 
        self.image = pygame.image.load(obstacle)
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,420-40)
                                                 , 0))
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 400 - 40), 0)


class Enemy2(pygame.sprite.Sprite):
      def __init__(self,obstacle):
        super().__init__()
        self.image = pygame.image.load(obstacle)
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (random.randint(40,420-40)
                                                 , 0))

 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED + 1)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 400 - 40), 0)

                

max = Player()
E1 = Enemy("Enemy.png")
TREE1 = Tree("cacto_1.png")
E2 = Enemy2("Enemy2.png")

enemies = pygame.sprite.Group()
enemies.add(E1)
enemies.add(E2)
all_sprites = pygame.sprite.Group()
all_sprites.add(max)
all_sprites.add(E1)
all_sprites.add(TREE1)
all_sprites.add(E2)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if SCORE % 10 == 0:
              SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        print(entity.rect)
        entity.move()

    # if pygame.sprite.spritecollideany(max, enemies):
    if max.rect[1] in range(E1.rect[1], E1.rect[-1]) or max.rect[-1] in range(E1.rect[1], E1.rect[-1]):
        pygame.mixer.Sound('crash.wav').play()
        max.image = pygame.image.load('explosion.png')
        DISPLAYSURF.blit(max.image, max.rect)
        pygame.display.update()
        time.sleep(2)     
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

          
                  
    pygame.display.update()
    FramePerSec.tick(FPS)

    

