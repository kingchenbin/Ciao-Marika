import pygame
from pygame.locals import *
import math
import random
import time

pygame.init()
width, height = 640, 640
screen=pygame.display.set_mode((width, height))

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

running = 1
exitcode = 0
while running:
    badtimer-=1
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the player on the screen at X:100, Y:100
    for x in range(width/grass.get_width()+1):
        for y in range(height/grass.get_height()+1):
            screen.blit(grass,(x*100,y*100))
    pos = list(playerpos);
    screen.blit(snake_node, pos)
    print '0', pos
    for i in range(0, length-1):
        if keys[i] == 0:
            pos[1] += 10
        elif keys[i] == 1:
            pos[1] -= 10
        if keys[i] == 2:
            pos[0] += 10
        elif keys[i] == 3:
            pos[0] -= 10
        screen.blit(snake_node, pos)
        print i+1, pos
    print 'before draw', keys

    # 7 - update the screen
    pygame.display.flip()
    
    time.sleep(0.6)
    kick = False
    print 'b2', playerpos
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
                print 'BLANK!'
    print 'b3', playerpos
    if kick==True:
        keys.pop()
        keys.insert(0, key)
        print keys
    else:
        currentKey = keys[0]
        keys.pop()
        keys.insert(0, currentKey)
        
    print 'after event', playerpos
    print 'after event', keys
    # 9 - Move player
    if keys[0]==0:
        print 'AA'
        playerpos[1]-=10
    elif keys[0]==1:
        print 'BB'
        playerpos[1]+=10
    if keys[0]==2:
        print 'CC'
        playerpos[0]-=10
    elif keys[0]==3:
        print 'DD'
        playerpos[0]+=10
    print 'after process', playerpos
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