import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption('Simulación Buzo')


mar = pygame.image.load('mar.jpg')
mar = pygame.transform.scale(mar, (800, 600))


myfont = pygame.font.SysFont("monospace", 20)
def profundidad(y):
    label = myfont.render("Profundidad: " + str(int(y)) + "mts", 1, (0,0,0))
    screen.blit(label, (50, 50))

myfont = pygame.font.SysFont("monospace", 20)
def presion(y):
    label = myfont.render("Presión: " + str(int(y * 9.806)) + "kPa", 1, (0,0,0))
    screen.blit(label, (50, 80))


playerImg = pygame.image.load('snorkel.png')
playerImg = pygame.transform.scale(playerImg, (60, 60))
playerX = 350
playerY = 250
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

running = True
while running:
    screen.blit(mar, (0, 0))

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


    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)

    profundidad(playerY)
    presion(playerY)

    pygame.display.update()