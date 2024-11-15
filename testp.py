import os
import random

count = 1000
history = {}
def clean():
	for i in range(10):
		history[str(i)] = 0
clean()
for i in range(10):	
	for i in range(count):
		history[str(random.randint(0,9))] += 1
	print(f"""
		p 0 - {history['0']/count}
		p 1 - {history['1']/count}
		p 2 - {history['2']/count}
		p 3 - {history['3']/count}
		p 4 - {history['4']/count}
		p 5 - {history['5']/count}
		p 6 - {history['6']/count}
		p 7 - {history['7']/count}
		p 8 - {history['8']/count}
		p 9 - {history['9']/count}""")
	clean()	