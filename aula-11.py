import pygame
import random
import math

#init
pygame.init()
#display
display_width = 640
display_height = 480
#cores
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
#setup
gameDisplay = pygame.display.set_mode((display_width,display_height))
gameDisplay.fill(white)
pygame.display.update()
pygame.display.set_caption('GAME-BASIC')
#relogio
clock = pygame.time.Clock()
#imagens
heroi = pygame.image.load('emoji.png')
#dados do heroi
x = 200
y = 200
x_change = 0
y_change = 0

#****FUNCOES****#
#desenha o heroi na posicao x,y da tela
def desenha_heroi(x,y):
    pygame.draw.circle(gameDisplay,black,(x+13,y+14),17,0)
    gameDisplay.blit(heroi, (x,y))

def desenha_limites():
    pygame.draw.line(gameDisplay,black,(20,20),(620,20),1)
    pygame.draw.line(gameDisplay,black,(20,460),(620,460),1)
    pygame.draw.line(gameDisplay,black,(20,20),(20,460),1)
    pygame.draw.line(gameDisplay,black,(620,20),(620,460),1)

def desenha_ouros(ouros):
    for ouro in ouros:
       pygame.draw.circle(gameDisplay,black,(ouro[0],ouro[1]),8,0)
       pygame.draw.circle(gameDisplay,yellow,(ouro[0],ouro[1]),6,0)

def desenha_score(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE: "+str(score), True, black)
    gameDisplay.blit(text,(20,1))

def ultrapassou_limite_X(meu_x,deslocamento):
    if(meu_x+deslocamento>=600 or meu_x+deslocamento<=15):
        return True
    return False

def ultrapassou_limite_Y(meu_y,deslocamento):
    if(meu_y+deslocamento<=15 or meu_y+deslocamento>=440):
        return True
    return False

def criar_ouros():
    ouros = []
    for i in range(10):
        tx = random.randint(50,600)
        ty = random.randint(50,440)
        ouros.append([tx,ty])
    return ouros

def calcula_distancia(x1,x2,y1,y2):
    dist = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    return dist

def testa_colisao_com_ouros(eux,euy,ouros):
    remove = 0
    for ouro in ouros:
        if(calcula_distancia(eux,ouro[0]-12,euy,ouro[1]-12)<=25):
            remove = ouro
            break
    if(remove != 0):
        ouros.remove(remove)
        return True
    return False

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
   
def mostra_mensagem(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    


#****PRINCIPAL****#
inicia = False
acabou = False
ganhou = False
#tela do menu
while not inicia:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inicia = True
            acabou = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                inicia = True
    mostra_mensagem("PRESSIONE 'S'")
    pygame.display.update()


fim = False
#tela do jogo
ouros = criar_ouros()
score = 0
while not fim and not acabou :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fim = True
    
        #imprimindo os eventos em tela
        #print(event)
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
    #colisao
    if(x_change!=0 or y_change!=0):
       if(testa_colisao_com_ouros(x,y,ouros)==True):
           score = score + 10
       if (score == 100):
           ganhou = True
           fim = True
    #desenha objetos
    desenha_limites()
    desenha_ouros(ouros)
    desenha_heroi(x,y)
    desenha_score(score)
    #atualiza a tela
    pygame.display.update()
    #60 frames per second
    clock.tick(60)

if ganhou:
    sai = False
    while not sai:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sai = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    sai = True
        mostra_mensagem("GANHOU! 'X' para sair.")
        pygame.display.update()

#finaliza de forma segura
pygame.quit()
quit()
