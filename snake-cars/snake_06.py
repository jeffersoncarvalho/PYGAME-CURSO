# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 15:07:41 2016

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
pygame.display.set_caption('SNAKE 06')
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

def snake_self_bite(snake, candidato):
    for ponto in snake:
        if ponto[0]==candidato[0] and ponto[1] == candidato[1]:
            return True
    return False

def game_loop():
    
    finished = False
    direction = 0
    score = 0
    #x = (display_width * 0.45)
    #y = (display_height * 0.8)

    x = 300
    y = 200    
    
    snake = [[x,y,direction]]
    snake_size = 1
    x_change = 0
    y_change = 0
    food_x = random.randrange(20, 110)*5
    food_y = random.randrange(20, 80)*5
    
    while not finished:

        candidatos = [[x+pixel_factor,y,1],[x-pixel_factor,y,0],[x,y+pixel_factor,3],[x,y-pixel_factor,2]]
        distancias = []
        dist_cand = {}
        for candidato in candidatos:
            if snake_size > 1:
                if (candidato[2]==1 and direction==0) or (candidato[2]==0 and direction==1):
                    continue
                if (candidato[2]==2 and direction==3) or (candidato[2]==3 and direction==2):
                    continue
                if snake_self_bite(snake,candidato):
                    continue
            distancia = distancia_dois_pontos(candidato[0],food_x,candidato[1],food_y)
            distancias.append(distancia)
            dist_cand[distancia] = candidato
        distancias.sort()
        melhor = dist_cand[distancias[0]]     
        direction = melhor[2]
        
        
            
        if(x+x_change<display_width-30 and x+x_change>=0 and
           y+y_change<display_height-30 and y+y_change>=50):
               for i in range(len(snake)-1,0,-1):
                   snake[i][0] = snake[i-1][0]
                   snake[i][1] = snake[i-1][1] 
                   snake[i][2] = snake[i-1][2]
               x = melhor[0]
               y = melhor[1]
               snake[0][0] = x
               snake[0][1] = y
               snake[0][2] = direction
              
                
               
        gameDisplay.fill(white)
       
        for ponto in snake:
            draw_emoji(ponto[0],ponto[1])

       
        
        draw_food(food_x,food_y)
        
        if colidiu(x,y,food_x,food_y,pixel_factor):
            #print "COLISAO"
            food_x = random.randrange(20, 110)*5
            food_y = random.randrange(20, 80)*5
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
        clock.tick(60)

#MAIN
game_loop()
pygame.quit()
quit()