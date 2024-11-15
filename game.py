# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random
import os

#физика
g=3.14
m=2

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
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
FPS = 60
speed= 3

player_img = pygame.image.load(os.path.join(img_folder, 'image5.png')).convert_alpha()
key_img1 =pygame.image.load(os.path.join(img_folder,'Key_left.png')).convert_alpha()
key_img2 =pygame.image.load(os.path.join(img_folder,'Key_up.png')).convert_alpha()
sky_img=pygame.image.load(os.path.join(img_folder,'sky.png')).convert()
block_img=pygame.image.load(os.path.join(img_folder,'block.png')).convert()
trava_img=pygame.image.load(os.path.join(img_folder,'trava.png')).convert_alpha()
oblako_img=pygame.image.load(os.path.join(img_folder,'oblako.png')).convert_alpha()


scale_player=pygame.transform.scale(player_img,(100, 200))

scale_key_left=pygame.transform.scale(key_img1,(400, 230))

scale_key_right=pygame.transform.scale(key_img1,(400, 230))

scale_key_up=pygame.transform.scale(key_img2,(190, 190))

sky_scale=pygame.transform.scale(sky_img,(WIDTH, HEIGHT))

oblako_scale=pygame.transform.scale(oblako_img,(880,700))


key_right_img=pygame.transform.rotate(scale_key_right, 90)

key_left_img=pygame.transform.rotate(scale_key_left, 270)

key_up_img=pygame.transform.rotate(scale_key_up, -90)

geib=pygame.transform.rotate(scale_player, 270)

block=pygame.transform.rotate(block_img,270)

trava=pygame.transform.rotate(trava_img,270)

oblako=pygame.transform.rotate(oblako_scale,270)

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group() 
blocks= pygame.sprite.Group()
keys=pygame.sprite.Group()
width_geib=geib.get_width()
rect= pygame.Rect((0,-100,200,300))
rect1= pygame.Rect((-3.5,150,200,300))
rect_pl=pygame.Rect((450,50,90,48))

class Player(pygame.sprite.Sprite):
	def __init__(self):
        	pygame.sprite.Sprite.__init__(self)
        	self.image = geib
        	self.rect = rect_pl 
        	
	def update(self):
	    	if self.rect.top >HEIGHT -width_geib // 3:
	    		self.rect.bottom =0 + width_geib // 3
	    	elif self.rect.right< 0:
	    		self.rect.center=(450,50)


class Key_left(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=key_left_img
		self.rect = rect
		

class Key_right(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image=key_right_img
		self.rect = rect1

class Key_up(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= key_up_img
		self.rect = self.image.get_rect()
		self.rect.center=(290,HEIGHT - 120)
	
class Sky(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= sky_scale
		self.rect= self.image.get_rect()

class Block(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= block
		self.rect = self.image.get_rect()
		self.rect.x = 200

class Trava(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= trava
		self.rect=pygame.Rect((300,300,30,30))

class Oblako(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= oblako
		self.rect=self.image.get_rect()
		self.rect.center=(530,500)
player=Player()
key_left=Key_left()
key_right=Key_right()
oblako1=Oblako()
sky=Sky()
key_up=Key_up()

trava_=Trava()
block1=Block()

block2=Block()
block2.rect.y+=100
trava_1=Trava()
trava_1.rect.y+=100

block3=Block()
block3.rect.y+=200
trava_2=Trava()
trava_2.rect.y+=250

block4=Block()
block4.rect.y+=300

block5=Block()
block5.rect.y+=400

block6=Block()
block6.rect.y+=500

block7=Block()
block7.rect.y+=600
	
all_sprites.add(sky)
all_sprites.add(oblako1)
blocks.add(block1)
blocks.add(block2)
blocks.add(block3)
blocks.add(block4)
blocks.add(block5)
blocks.add(block6)
blocks.add(block7)
all_sprites.add(trava_)
all_sprites.add(trava_1)
all_sprites.add(trava_2)
all_sprites.add(player)
keys.add(key_left)
keys.add(key_right)
keys.add(key_up)

def jump(player,jumpforce):
	player.rect.x +=jumpforce

# Цикл игры
running = True
touched=False
left=False
right=False
up=False
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            touched=True
            
            if key_left.rect.collidepoint(event.pos):
                left= True
                
            if key_right.rect.collidepoint(event.pos):
                right= True
                
            if key_up.rect.collidepoint(event.pos):
                up = True
                
        elif event.type == pygame.MOUSEBUTTONUP:
        	touched=False
        	left=False
        	right=False
        	up=False
    on_ground=pygame.sprite.spritecollide(player,blocks,False)
    

    # Обновление
    all_sprites.update()
    keys.update()
    blocks.update()
    
    if on_ground:
    	if up:
    		player.rect.x+= 10
    		player.rect.x+= 80
    		up=False
    elif up ==False:
    	Ft=m*g
    	player.rect.x-= Ft
    # Рендеринг
    screen.fill(WHITE)
    if touched:
        	if left:
        		player.rect.y-= speed
        	if right:
        		player.rect.y+= speed
    
    all_sprites.draw(screen)
    blocks.draw(screen)
    keys.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()

pygame.quit()