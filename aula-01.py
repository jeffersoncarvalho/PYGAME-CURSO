import pygame
import time


#init
pygame.init()
#display
display_width = 640
display_height = 480
#setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill((255,255,255))
pygame.display.update()
pygame.display.set_caption('GAME-BASIC')

time.sleep(5)

pygame.quit()
quit()
