import pygame
import random
 
 
# здесь будут рисоваться фигуры
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230) 
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
pygame.init()
 
clock = pygame.time.Clock()
 
sc = pygame.display.set_mode((640, 480))

FPS = 60
WIN_WIDTH = sc.get_width()
WIN_HEIGHT = sc.get_height()
put="start"
put_x="start"
 
# радиус и координаты круга
r = 30
x = 30
y = 0  
 
while 1:
    sc.fill(WHITE)
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT: exit()
 
    pygame.draw.circle(sc, ORANGE, (x, y), r)
 
    pygame.display.update()
 
    # если полностью скрылся за правой границей
    if y >= WIN_HEIGHT:
    	put="back"
    elif y <= 0:
        put="start"
    if put == "start":
    	y += 2
    elif put == "back":
    	y -= 2
    if x >=WIN_WIDTH:
    	put_x="back"
    elif x <= 0:
    	put_x="start"
    if put_x=="back":
    	x-=0.5
    elif put_x=="start":
    	x+=0.5
 
    clock.tick(FPS)

pygame.display.update()