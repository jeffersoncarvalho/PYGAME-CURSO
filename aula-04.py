import pygame

#init
pygame.init()
#display
display_width = 640
display_height = 480
#cores
black = (0,0,0)
white = (255,255,255)
#setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
pygame.display.update()
pygame.display.set_caption('GAME-BASIC')
#relogio
clock = pygame.time.Clock()
#imagens
heroi = pygame.image.load('emoji.png')
#dados dos heroi
x = 50
y = 50

#****FUNCOES****#
#desenha o heroi na posicao x,y da tela
def desenha_heroi(x,y):
    gameDisplay.blit(heroi, (x,y))

#****PRINCIPAL****#
fim = False
while not fim:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True
        #imprimindo os eventos em tela
        print(event)
        #pressionou a tecla (no entanto, nao eh o ideal)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x-5
            elif event.key == pygame.K_RIGHT:
                x = x+5
    #apaga a tela
    gameDisplay.fill(white)
    #desenha
    desenha_heroi(x,y)
    #atualiza a tela
    pygame.display.update()
    #60 frames per second
    clock.tick(60)

#finaliza de forma segura
pygame.quit()
quit()
