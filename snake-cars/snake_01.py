# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 13:53:04 2016

@author: jefferson
"""

import pygame

pygame.init()

display_width = 640
display_height = 480

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('SNAKE 01')
clock = pygame.time.Clock()
emojiFaceImg = pygame.image.load('emoji.png')

def draw_emoji(x,y):
    gameDisplay.blit(emojiFaceImg,(x,y))

def draw_rect(x, y, width, height, color):
    pygame.draw.rect(gameDisplay, color, [x, y, width, height])

def game_loop():
    
    finished = False
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    
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

        x += x_change
        y += y_change
        gameDisplay.fill(white)
        #draw_rect(x,y,50,50,black)
        draw_emoji(x,y)
        
        pygame.display.update()
        clock.tick(60)

#MAIN
game_loop()
pygame.quit()
quit()
        
        
        