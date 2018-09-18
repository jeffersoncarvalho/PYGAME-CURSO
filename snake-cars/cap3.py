import pygame

pygame.init()

display_width = 640
display_height = 480

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('racecar.png')





def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x =  (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
car_speed = 0

while not crashed:
    
    #for de eventos
    for event in pygame.event.get():

        #termina o while
        if event.type == pygame.QUIT:
            crashed = True

        ############################
        #pressionou a tecla
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        #soltou a tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        ######################

    ##
    #faz o carro mover            
    x += x_change
    ##

    #atualiza posicao do carro
    gameDisplay.fill(white)
    car(x,y)

    #renderiza a tela
    pygame.display.update()
    # espera 60 ms para update
    clock.tick(60)

pygame.quit()
#quit()


