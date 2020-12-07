import pygame
from parametros import *
from clases import Button

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Simulación Buzo')
botella_apretada = False

### Botones
button1 = Button((750, 40), (40, 40), 'water.png')
button2 = Button((750, 90), (40, 40), 'snorkel.png')


mar = pygame.image.load('mar.jpg')
mar = pygame.transform.scale(mar, (800, 600))

myfont = pygame.font.SysFont("monospace", 15)
cosas = myfont.render('Cambia el objeto:', 1, (0,0,0))


myfont = pygame.font.SysFont("monospace", 20)
def profundidad(y):
    label = myfont.render("Profundidad: " + str(int(y)) + "mts", 1, (0,0,0))
    screen.blit(label, (50, 50))

myfont = pygame.font.SysFont("monospace", 20)
def presion(y):
    label = myfont.render("Presión: " + str(int(y * rho * g + p_atm)) + "kPa", 1, (0,0,0))
    screen.blit(label, (50, 80))

myfont = pygame.font.SysFont("monospace", 20)
def volumen(y):
    label = myfont.render("Volumen botella: " + str(round((int(R * T * n)/int(y * rho * g + p_atm)),2)) + " L", 1, (0,0,0))
    screen.blit(label, (50, 110))


buzo = pygame.image.load('snorkel.png')
buzo = pygame.transform.scale(buzo, (60, 60))
botella = pygame.image.load('water.png')
botella = pygame.transform.scale(botella, (60, 60))

playerX = 350
playerY = 0
playerX_change = 0
playerY_change = 0

def player(x, y):
    if button1.apretado == False and button2.apretado == False:
        screen.blit(buzo, (x, y))
        
    if button2.apretado == True:
        screen.blit(buzo, (x, y))
        button1.apretado = False
        
    if button1.apretado == True:
        screen.blit(botella, (x, y))
        button2.apretado = False
        botella_apretada = True

      


######### LOOP PRINCIPAL ##########
running = True
while running:
    screen.blit(mar, (0, 0))
    screen.blit(cosas, (640, 10))

### Movimiento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.4
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.4
            if event.key == pygame.K_DOWN:
                playerY_change = 0.4
            if event.key == pygame.K_UP:
                playerY_change = -0.4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0

        #handler de botones
        button1.event_handler(event)
        button2.event_handler(event)


    playerX += playerX_change
    playerY += playerY_change

### Limites de la pantalla
    if  playerX < 0:
        playerX = 0
    elif playerX > 740:
        playerX = 740
    if playerY < 0:
        playerY = 0
    elif playerY > 540:
        playerY = 540

    player(playerX, playerY)

    profundidad(playerY)
    presion(playerY)
    if botella_apretada is True:
        volumen(playerY)
    

    button1.draw(screen)
    button2.draw(screen)

    pygame.display.update()

    