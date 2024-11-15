import os
import random

class color:
	Red = '\033[91m'
	Green = '\033[92m'
	Yellow = '\033[93m'
	Blue = '\033[94m'
	Magenta = '\033[95m'
	Cyan = '\033[96m'
	White = '\033[97m'
	Grey = '\033[90m'
	BOLD = '\033[1m'
	ITALIC = '\033[3m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'

class entities:
	food = color.Green + "©" + color.END
	free = color.White + "•" + color.END

def draw(game_map):
	os.system("clear")
	for i in game_map:
		cur_row = ""
		for j in i:
			cur_row += j
		print(cur_row)

def create_map(x, y) -> list:
	game_map = []
	for height in range(0,y+1):
		cur_raw = []
		for i in range(0,x):
			random.choice(entities)
			cur_raw.append(i)
		game_map.append(cur_raw)
	return game_map

create_map(5,10)