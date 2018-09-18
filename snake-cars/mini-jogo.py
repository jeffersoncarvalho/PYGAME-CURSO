# -*- coding: utf-8 -*-
import pygame
import random

pygame.init()

width = 640
height = 480

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

pixel_factor = 10

posX = 100
posY = 100

foodX = 250
foodY = 300

enemies = [[20,20],[300,300],[400,200]]

gameDisplay = pygame.display.set_mode((width,height))
gameDisplay.fill(white)

pygame.display.update()
pygame.display.set_caption('PRIMEIRO JOGO')

clock = pygame.time.Clock()

def move_enemies():
    
    for enemy in enemies:
        x = random.randint(1,5)
        if(x==1):
            if not (enemy[1] + pixel_factor>=height-40):
                enemy[1] = enemy[1] + pixel_factor
        elif(x==2):
            if not (enemy[1] + pixel_factor<40):
                enemy[1] = enemy[1] - pixel_factor
        elif(x==3):
            if not (enemy[0] + pixel_factor>=width-40):
                enemy[0] = enemy[0] + pixel_factor
        else:
            if not (enemy[0] + pixel_factor<40):
                enemy[0] = enemy[0] - pixel_factor
            
def draw_enemies():
    for enemy in enemies:
        draw_rect(enemy[0],enemy[1],blue)

def detect_collision():
    global foodX
    global foodY
    if(posX == foodX and posY == foodY):
        foodX = random.randrange(1,60)*pixel_factor
        foodY = random.randrange(1,40)*pixel_factor
        

def draw_food():
    draw_rect(foodX,foodY,green)

def move_up():
    global posY
    if not(posY-pixel_factor<0):
        posY = posY - pixel_factor
def move_down():
    global posY
    if not(posY+pixel_factor>=height):
        posY = posY + pixel_factor
def move_left():
    global posX
    if not(posX-pixel_factor<0):
        posX = posX - pixel_factor
def move_right():
    global posX
    if not(posX+pixel_factor>=width):
        posX = posX + pixel_factor

def draw_rect(x,y,color):
    pygame.draw.rect(gameDisplay,color,[x,y,pixel_factor,pixel_factor])

def draw_grid():
    
    for x in range(10,631,10):
        draw_line(x,0,x,479)
    for y in range(10,481,10):
        draw_line(0,y,639,y)

def draw_line(xI,yI,xF,yF):
    pygame.draw.line(gameDisplay,black,(xI,yI),(xF,yF),1)    
    

def game_loop():
    
    while True:
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            move_up()
            detect_collision()
        if keys[pygame.K_DOWN]:
            move_down()
            detect_collision()
        if keys[pygame.K_LEFT]:
            move_left()
            detect_collision()
        if keys[pygame.K_RIGHT]:
            move_right()
            detect_collision()
        
        gameDisplay.fill(white)
        #MUDANÇA NO CENÁRIO - INÍCIO
        draw_grid()   
        draw_rect(posX,posY,red)
        draw_food()
        move_enemies()
        draw_enemies()
        #MUDANÇA NO CENÁRIO - FIM
        pygame.display.update()
        pygame.display.flip()
        clock.tick(20)
        pygame.event.pump()

#PRINCIPAL
game_loop()




















