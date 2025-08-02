import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("UFO.png")
pygame.display.set_icon(icon)
playerImage= pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change=0
def player(x,y):
    screen.blit(playerImage,(x,y))
enemyImage= pygame.image.load("Enemy.png")
enemyX =random.randint(0,800)
enemyY =random.randint(50,150)
enemyX_change=0.3
enemyY_change=40
def enemy(x,y):
    screen.blit(enemyImage,(x,y))    
done = True
while done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-0.1
            if event.key==pygame.K_RIGHT:
                playerX_change=0.1    
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change = 0 
    screen.fill((255,0,0))
    if playerX<=0:
        playerX = 0
    elif playerX>=736:
        playerX=736
    playerX+=playerX_change
    player(playerX,playerY)
    if enemyX<=0:
        enemyX_change=0.3
        enemyY+=enemyY_change
    elif enemyX>=736:
        enemyX_change=-0.3
        enemyY+=enemyY_change
    enemyX+=enemyX_change
    enemy(enemyX,enemyY)
    pygame.display.update() 