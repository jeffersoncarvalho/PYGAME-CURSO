import pygame


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
#relogio
clock = pygame.time.Clock()

fim = False
while not fim:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True
    #imprimindo os eventos em tela
    print(event)
    #atualiza a tela
    pygame.display.update()
    #60 frames per second
    clock.tick(60)

#finaliza de forma segura
pygame.quit()
quit()
