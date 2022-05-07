import pygame
import sys

pygame.init()

WHITE = (255, 255, 255)
BLACK   = (  0,  0,  0)
RED = (255,  0,  0)

size = (800, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

#------------------------CORDS--------------------------------------------------
coordx = 10
coordy = 200
coordx2 = 760
coordy2 = 200
circlecoordx = 400
circlecoordy = 250

#------------------------SPEED--------------------------------------------------
speedy = 0
speedy2 = 0
circlespeedx = 3
circlespeedy = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#------------------------KEYS---------------------------------------------------
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                speedy = -4
            if event.key == pygame.K_s:
                speedy = 4
            if event.key == pygame.K_UP:
                speedy2 = -4
            if event.key == pygame.K_DOWN:
                speedy2 = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                speedy = 0
            if event.key == pygame.K_s:
                speedy = 0
            if event.key == pygame.K_UP:
                speedy2 = 0
            if event.key == pygame.K_DOWN:
                speedy2 = 0


    screen.fill(BLACK)

#------------------------MOVEMENT-----------------------------------------------
    coordy2 += speedy2
    coordy += speedy
    circlecoordx += circlespeedx
    circlecoordy += circlespeedy
    
#------------------------ROOF COLISIONS-----------------------------------------
    if (coordy > 400 or coordy < 0):
        speedy *= 0
    if (coordy2 > 400 or coordy2 < 0):
        speedy2 *= 0
    if (circlecoordy > 500 or circlecoordy < 0):
        circlespeedy *= -1

#------------------------WALL & RECOVER-----------------------------------------
    if circlecoordx > 800:
        circlecoordx = 400
        circlecoordy = 250

        circlespeedx *= -1
        circlespeedy *= -1

    if circlecoordx < 0:
        circlecoordx = 400
        circlecoordy = 250

        circlespeedx *= -1
        circlespeedy *= -1

#------------------------FIGURES------------------------------------------------
    circle = pygame.draw.circle(screen, WHITE, (circlecoordx, circlecoordy), 10)
    p1 = pygame.draw.rect(screen, WHITE, (coordx, coordy, 25, 100))
    p2 = pygame.draw.rect(screen, WHITE, (coordx2, coordy2, 25, 100))

#------------------------COLISIONS----------------------------------------------
    if circle.colliderect(p1) or circle.colliderect(p2):
        circlespeedx *= -1



    pygame.display.flip()
    clock.tick(60)
