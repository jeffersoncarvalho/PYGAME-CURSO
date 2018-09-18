# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:16:52 2016

@author: jefferson
"""

import pygame
import random
import math



pygame.init()

display_width = 640
display_height = 480

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SNAKE 03')
clock = pygame.time.Clock()
emojiFaceImg = pygame.image.load('emoji.png')

def show_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE: "+str(score), True, black)
    gameDisplay.blit(text,(10,10))

def distancia_dois_pontos(x1, x2, y1, y2):
    dist = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)
    return math.sqrt(dist)

def colidiu(x1, y1, x2, y2, fator):
    dist = distancia_dois_pontos(x1,x2,y1,y2)
    if dist<=fator:
        return True
    return False
    
def draw_emoji(x,y):
    gameDisplay.blit(emojiFaceImg,(x,y))

def draw_rect(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def draw_food(x,y):
    draw_rect(x,y,30,30,red)

def game_loop():
    
    finished = False
    score = 0
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    food_x = random.randrange(0, display_width)
    food_y = random.randrange(0, display_height)
    
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

        if(x+x_change<display_width-30 and x+x_change>=0 and
           y+y_change<display_height-30 and y+y_change>=50):
               x += x_change
               y += y_change
               
        gameDisplay.fill(white)
        #draw_rect(x,y,50,50,black)
        draw_emoji(x,y)
        draw_food(food_x,food_y)
        
        if colidiu(x,y,food_x,food_y,30):
            #print "COLISAO"
            food_x = random.randrange(80, display_width-30)
            food_y = random.randrange(80, display_height-30)
            score += 10
        
        show_score(score)
        pygame.display.update()
        clock.tick(60)

#MAIN
game_loop()
pygame.quit()
quit()