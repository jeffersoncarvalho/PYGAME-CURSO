# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 16:09:38 2016

@author: jefferson
"""

import pygame


#init
pygame.init()
#display
display_width = 640
display_height = 480
#colors
black = (0,0,0)
white = (255,255,255)
red = (150,0,0)
blue = (0,0,200)
green = (0,150,0)
#game
pixel_factor = 10
posX = 100
posY = 100
#setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
pygame.display.update()
pygame.display.set_caption('GAME-BASIC')
clock = pygame.time.Clock()

def draw_boundaries():
    pygame.draw.line(gameDisplay,black,(20,20),(620,20),1)
    pygame.draw.line(gameDisplay,black,(20,460),(620,460),1)
    pygame.draw.line(gameDisplay,black,(20,20),(20,460),1)
    pygame.draw.line(gameDisplay,black,(620,20),(620,460),1)

def draw_grid():
    
    for y in range(20,461,10):
        pygame.draw.line(gameDisplay,black,(20,y),(620,y),1)
    for x in range(20,621,10):
        pygame.draw.line(gameDisplay,black,(x,20),(x,460),1)

def draw_rect(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])
    
def draw_hero(x,y):
    draw_rect(x,y,pixel_factor,pixel_factor,red)

def move_left():
    global posX
    posX = posX - 10
def move_right():
    global posX
    posX = posX + 10
def move_up():
    global posY
    posY = posY - 10
def move_down():
    global posY 
    posY = posY + 10

def game_loop():
    
    
    while True:
        keys = pygame.key.get_pressed()  #checking pressed keys
        if keys[pygame.K_UP]:
            move_up()
        if keys[pygame.K_DOWN]:
            move_down()
        if keys[pygame.K_LEFT]:
            move_left()
        if keys[pygame.K_RIGHT]:
            move_right()
        
       
        #draw_boundaries()
        gameDisplay.fill(white)
        draw_hero(posX,posY)
        draw_grid()
        pygame.display.update()
        pygame.display.flip()
        clock.tick(15)
        pygame.event.pump()
        
    
#PRINCIPAL
game_loop()

