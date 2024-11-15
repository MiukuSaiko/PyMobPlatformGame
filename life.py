import pygame 
import os
import random


game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'assets')


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


sc=pygame.display.set_mode((720,720))
WIDTH = sc.get_width()
HEIGHT = sc.get_height()
clock = pygame.time.Clock()

img_green=pygame.image.load(os.path.join(img_folder, 'green_bot.png')).convert_alpha()
img_blue=pygame.image.load(os.path.join(img_folder, 'blue_bot.png')).convert_alpha()
img_pink=pygame.image.load(os.path.join(img_folder, 'pink_bot.png')).convert_alpha()
eat_img=pygame.image.load(os.path.join(img_folder,'eat.png')).convert_alpha()


green_bot=pygame.transform.scale(img_green,(100,100))
blue_bot=pygame.transform.scale(img_blue,(100,100))
pink_bot=pygame.transform.scale(img_pink,(100,100))
cletka=pygame.transform.scale(eat_img,(30,30))

def rand(skin1,skin2,skin3):
	WIDTH = sc.get_width()
	HEIGHT = sc.get_height()
	bot_rand=random.randint(1,3)
	if bot_rand==1:
		return skin1
	elif bot_rand==2:
		return skin2
	elif bot_rand==3:
		return skin3


bots=pygame.sprite.Group()
eat=pygame.sprite.Group()


class Bot(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= rand(green_bot,blue_bot,pink_bot)
		self.rect = self.image.get_rect()
		self.speed=3
		self.hungry=100
		self.id=1
	def update(self):
		width=self.image.get_width()
		height=self.image.get_height()
		self.rect.x+=self.speed
		if self.rect.right > WIDTH + 100:
			self.rect.left = -50

bot=Bot()
bots.add(bot)


class Food(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image= cletka
		self.rect = self.image.get_rect()
		width=self.image.get_width()
		height=self.image.get_height()
		self.rect.x=random.randint(0,WIDTH - width)
		self.rect.y=random.randint(0,HEIGHT - height)


for i in range(30):
	f=Food()
	eat.add(f)


running=True
while running:
	clock.tick(30)
	for event in pygame.event.get():
	       # check for closing window
	       if event.type == pygame.QUIT:
	       	running = False
	bots.update()
	eat.update()
	
	eating=pygame.sprite.groupcollide(bots,eat,False,True)
	print(eating)
	       
	sc.fill(BLACK)
	bots.draw(sc)
	eat.draw(sc)
	       
	pygame.display.flip()