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
heroi = pygame.image.load('emoji-menor.png')
#dados dos heroi
x = 200
y = 200
x_change = 0
y_change = 0

#****FUNCOES****#
#desenha o heroi na posicao x,y da tela
def desenha_heroi(x,y):
    gameDisplay.blit(heroi, (x,y))

def desenha_limites():
    pygame.draw.line(gameDisplay,black,(20,20),(620,20),1)
    pygame.draw.line(gameDisplay,black,(20,460),(620,460),1)
    pygame.draw.line(gameDisplay,black,(20,20),(20,460),1)
    pygame.draw.line(gameDisplay,black,(620,20),(620,460),1)

def ultrapassou_limite_X(meu_x, deslocamento):
    if(meu_x+deslocamento>=600 or meu_x+deslocamento<=15):
        return True
    return False

def ultrapassou_limite_Y(meu_y, deslocamento):
    if(meu_y+deslocamento<=15 or meu_y+deslocamento>=440):
        return True
    return False


#****PRINCIPAL****#
fim = False
while not fim:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True
        ##imprimindo os eventos em tela
        print(event)
        #pressionou a tecla 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        #soltou a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_change = 0

    #apaga a tela
    gameDisplay.fill(white)
    #movimenta o heroi
    if not ultrapassou_limite_X(x,x_change):
        x = x + x_change
    if not ultrapassou_limite_Y(y,y_change):
        y = y + y_change
    #desenha objetos
    desenha_heroi(x,y)
    desenha_limites()
    #atualiza a tela
    pygame.display.update()
    #60 frames per second
    clock.tick(60)

#finaliza de forma segura
pygame.quit()
quit()
