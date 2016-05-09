import pygame
from pygame.locals import *
import math
import random
import time

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 640

def InitBarriers(playerpos, length):
	return [[10,0],[20,0]]

def CalcSnake(playerpos, keys, length):
	head = list(playerpos)
	snake = []
	snake.append(head)
	pos = list(head)
	for i in range(0, length-1):
		if keys[i] == 0:
			pos[1] += 10
		elif keys[i] == 1:
			pos[1] -= 10
		elif keys[i] == 2:
			pos[0] += 10
		elif keys[i] == 3:
			pos[0] -= 10
		tempPos = list(pos)
		snake.append(tempPos)
	return snake

def HitTest(snake, length, barriers):
	for i in range(0, length):
		print length, i, snake[i][0], snake[i][1]
		if snake[i][0] < 0:
			return False
		elif snake[i][0] >= WINDOW_WIDTH:
			return False
		elif snake[i][1] < 0:
			return False
		elif snake[i][1] >= WINDOW_HEIGHT:
			return False
		else:
			for j in range(0, length):
				if i != j and snake[i] == snake[j]:
					return False
			for brick in barriers:
				if brick == snake[i]:
					return False
	return True

def ShowBackground(cell):
	for x in range(WINDOW_WIDTH/cell.get_width()+1):
		for y in range(WINDOW_HEIGHT/cell.get_height()+1):
			screen.blit(cell,(x*100,y*100))

def ShowSnake(snake):
	for pos in snake:
		screen.blit(snake_node, pos)

pygame.init()
screen=pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# UP/0 DOWN/1 LEFT/2 RIGHT/3
key = 0
keys = [0, 0, 0, 0]
kick = False

length = 5
playerpos=[100,100]

acc=[0,0]
arrows=[]
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

# 3 - Load image
snake_node = pygame.image.load("resources/images/snake_node.png")
grass = pygame.image.load("resources/images/grass.png")

barriers=InitBarriers(playerpos,length)

running = 1
exitcode = 0
while running:
    badtimer-=1
    # 5 - clear the screen before drawing it again
    screen.fill(0)

    snake = CalcSnake(playerpos, keys, length)
    if True == HitTest(snake, length, barriers):
    	ShowBackground(grass)
    	ShowSnake(snake)
    else:
    	running = 0
    	break

    # 7 - update the screen
    pygame.display.flip()
    
    time.sleep(0.6)
    kick = False

    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key==K_w:
                if keys[0]!=0 and keys[0]!=1:
                    key=0
                    kick=True
            elif event.key==K_a:
                if keys[0]!=2 and keys[0]!=3:
                    key=2
                    kick=True
            elif event.key==K_s:
                if keys[0]!=0 and keys[0]!=1:
                    key=1
                    kick=True
            elif event.key==K_d:
                if keys[0]!=2 and keys[0]!=3:
                    key=3
                    kick=True
            elif event.key==K_SPACE:
                key = 0
                keys = [0, 0, 0, 0]
                kick = False
                length = 5
                playerpos=[100,100]
            elif event.key==K_RETURN:
            	currentKey = keys[length-2]
            	length += 1
            	keys.append(currentKey)

    if kick==True:
        keys.pop()
        keys.insert(0, key)
    else:
        currentKey = keys[0]
        keys.pop()
        keys.insert(0, currentKey)

    # 9 - Move player
    if keys[0]==0:
        playerpos[1]-=10
    elif keys[0]==1:
        playerpos[1]+=10
    if keys[0]==2:
        playerpos[0]-=10
    elif keys[0]==3:
        playerpos[0]+=10

    #10 - Win/Lose check
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0

print "Game Over!"
print "You LOSE!"