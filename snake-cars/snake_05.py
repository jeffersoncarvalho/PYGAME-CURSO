# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:20:57 2016

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

pixel_factor = 5



gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SNAKE 05')
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
     pygame.draw.rect(gameDisplay, black, [x, y, pixel_factor, pixel_factor])
    #gameDisplay.blit(emojiFaceImg,(x,y))

def draw_rect(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def draw_food(x,y):
    draw_rect(x,y,pixel_factor,pixel_factor,red)

def game_loop():
    
    finished = False
    direction = 0
    score = 0
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    snake = [[x,y,direction]]
    snake_size = 1
    x_change = 0
    y_change = 0
    food_x = random.randrange(80, display_width-50)
    food_y = random.randrange(80, display_height-50)
    
    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -pixel_factor
                    y_change = 0
                    direction = 0
                if event.key == pygame.K_RIGHT:
                    x_change = pixel_factor
                    y_change = 0
                    direction = 1
                if event.key == pygame.K_UP:
                    y_change = -pixel_factor
                    x_change = 0
                    direction = 2
                if event.key == pygame.K_DOWN:
                    y_change = pixel_factor
                    x_change = 0
                    direction = 3
                

           # if event.type == pygame.KEYUP:
            #    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
             #       x_change = 0
              #  if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
               #     y_change = 0

        
            
        if(x+x_change<display_width-30 and x+x_change>=0 and
           y+y_change<display_height-30 and y+y_change>=50):
               for i in range(len(snake)-1,0,-1):
                   snake[i][0] = snake[i-1][0]
                   snake[i][1] = snake[i-1][1] 
                   snake[i][2] = snake[i-1][2]
                   
                  
                       
               x += x_change
               y += y_change
               snake[0][0] = x
               snake[0][1] = y
               snake[0][2] = direction
              
                
               
        gameDisplay.fill(white)
       
        for ponto in snake:
            draw_emoji(ponto[0],ponto[1])

       
        
        draw_food(food_x,food_y)
        
        if colidiu(x,y,food_x,food_y,pixel_factor):
            #print "COLISAO"
            food_x = random.randrange(80, display_width-50)
            food_y = random.randrange(80, display_height-50)
            score += 10
            snake_size += 1
            ultimo = snake[len(snake)-1]
            if(ultimo[2]==0): #LEFT
                novo = [ultimo[0]+pixel_factor,ultimo[1],ultimo[2]]
                snake.append(novo)
            if(ultimo[2]==1): #RIGHT
                novo = [ultimo[0]-pixel_factor,ultimo[1],ultimo[2]]
                snake.append(novo)
            if(ultimo[2]==2): #UP
                novo = [ultimo[0],ultimo[1]+pixel_factor,ultimo[2]]
                snake.append(novo)
            if(ultimo[2]==3): #DOWN
                novo = [ultimo[0],ultimo[1]-pixel_factor,ultimo[2]]
                snake.append(novo)
            #print snake
                
        
        show_score(score)
        pygame.display.update()
        clock.tick(30)

#MAIN
game_loop()
pygame.quit()
quit()