import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("space invaders")
back = pygame.image.load("abcd.png")
img = pygame.image.load("abc.png")
pygame.display.set_icon(img)

playimg = pygame.image.load("uefo.png")
plax = 370
play = 480
plachan = 0

EnemyImg = []
enx = []
eny = []
enchax = []
ency = []
noOfEnemy = 6
for i in range(noOfEnemy):
    EnemyImg.append(pygame.image.load("enemy.png"))
    enx.append(random.randint(0, 729))
    eny.append(random.randint(50, 150))
    enchax.append(2)
    ency.append(40)

bulImg = pygame.image.load("bu.png")
bux = 0
buy = 480
bucha_x = 0
bucha_y = 5
bu_state = "ready"
score=0
fon=pygame.font.Font("freesansbold.ttf",32)
textx=10
texty=10
def scoreof(x,y):
    sc=fon.render("SCORE :"+str(score),True,(255,255,255))
    screen.blit(sc,(x,y))


def player(x, y):
    screen.blit(playimg, (x, y))


def enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def bullet(x, y):
    global bu_state
    bu_state = "fire"
    screen.blit(bulImg, (x + 16, y + 10))


def isCollison(enx, eny, bux, buy):
    dist = math.sqrt((math.pow(enx - bux, 2)) + (math.pow(eny - buy, 2)))
    if dist <= 27:
        return True
    else:
        return False


run = True
while run:
    screen.fill((250, 0, 0))
    screen.blit(back, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plachan = -2
            if event.key == pygame.K_RIGHT:
                plachan = 2
            if event.key == pygame.K_SPACE:
                if bu_state == "ready":
                    bux = plax
                    bullet(bux, buy)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                plachan = 0

    plax += plachan
    if plax <= 0:
        plax = 0
    elif plax >= 750:
        plax = 750
    for i in range(noOfEnemy):
        enx[i] += enchax[i]
        if enx[i] >= 729:
            enchax[i] = - 2
            eny[i] += ency[i]
        elif enx[i] <= 0:
            enchax[i] = 2
            eny[i] += ency[i]

        coll = isCollison(enx[i], eny[i], bux, buy)
        if coll:
            buy = 480
            bu_state = "ready"
            score+=1
            enx[i] = random.randint(0, 729)
            eny[i] = random.randint(50, 150)

        enemy(enx[i], eny[i],i)
    if buy <= 0:
        buy = 480
        bu_state = "ready"
    if bu_state == "fire":
        bullet(bux, buy)
        buy -= bucha_y

    player(plax, play)
    scoreof(textx,texty)
    pygame.display.update()
