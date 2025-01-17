# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'assets')

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((720, 720))

player_img = pygame.image.load(os.path.join(img_folder, 'image5.png')).convert()
key_img1 =pygame.image.load(os.path.join(img_folder,'Key_left.png'))
key_img2 =pygame.image.load(os.path.join(img_folder,'Key_right.png'))

WIDTH = screen.get_width()
HEIGHT = screen.get_height()
FPS = 30
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 

class Player(pygame.sprite.Sprite):
	def __init__(self):
        	pygame.sprite.Sprite.__init__(self)
        	self.image = player_img
        	self.image.set_colorkey(BLACK)
        	self.rect = self.image.get_rect()
        	self.rect.center = (WIDTH / 2, HEIGHT / 2)
	def update(self):
	    	self.rect.x+=1
	    	if self.rect.left >WIDTH:
	    		self.rect.right =0
class Key_left(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=key_img1
		self.image.set_colorkey(BLACK)
		self.rect=self.image.get_rect()
		self.rect = self.image.get_rect()
		self.rect.center = (50, HEIGHT - 100)
 
player=Player()
key_left=Key_left()
all_sprites.add(player)
all_sprites.add(key_left)

# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Обновление
    all_sprites.update()
    # Рендеринг
    screen.fill(GREEN)
    all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()