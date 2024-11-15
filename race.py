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


player_img = pygame.image.load(os.path.join(img_folder, 'image5.png')).convert_alpha()
key_img1 =pygame.image.load(os.path.join(img_folder,'Key_left.png')).convert_alpha()

wheel_img= pygame.image.load(os.path.join(img_folder,'car-lowrider-tire.png'))
wheel= pygame.transform.scale(wheel_img,(60,60))

chassi_img= pygame.image.load(os.path.join(img_folder,'Car_state.png'))
chassi_rotate=pygame.transform.rotate(chassi_img,-90)
chassi=pygame.transform.scale(chassi_rotate,(200,310))

key_scale=pygame.transform.scale(key_img1,(400,230))
key_left=pygame.transform.rotate(key_scale,-90)

WIDTH = screen.get_width()
HEIGHT = screen.get_height()
FPS = 30
pygame.display.set_caption("Race")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 
car=pygame.sprite.Group()


class Key_left(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=key_left
		self.rect=pygame.Rect((0,-100,200,300))

class Wheel(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=wheel
		self.rect=self.image.get_rect()
		
wheel_left=Wheel()
wheel_left.rect.y=26
wheel_left.rect.x=223
wheel_right=Wheel()
wheel_right.rect.x=223
wheel_right.rect.y=220

class Chassi(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= chassi
		self.rect=self.image.get_rect()

chassi_main=Chassi()
chassi_main.rect.x=250

key_left=Key_left()
car.add(chassi_main)
car.add(wheel_left)
car.add(wheel_right)
all_sprites.add(key_left)

# Цикл игры
left=False
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            if key_left.rect.collidepoint(event.pos):
                left= True

    # Обновление
    all_sprites.update()
    car.update()
    # Рендеринг
    screen.fill(GREEN)
    if left:
    	
    all_sprites.draw(screen)
    car.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()