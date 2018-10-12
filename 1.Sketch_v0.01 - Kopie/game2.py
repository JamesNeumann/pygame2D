import pgzrun
import pygame
import time
import numpy


#Das ist ein Test und kann wieder gelöscht werden

WIDTH = 1200
HEIGHT = 700
GRAVITY = 2.5
FLAP_VELOCITY = -10.5

walls = []
stones = []
coins = []
grounds = []

level = [
    "I                                    CCC                             I",
    "I                                  WWWWWW                            I",
    "I                               WWWGGGGGG                            I",
    "I                 WWWWWW    WWWWGGGGGGGGG                            I",
    "I              _  IGGG                                               I",
    "I            __W                                                     I",
    "I          __IWG                                                     I",
    "I   ___    WWGGG                                                     I",
    "I   IWW   _GG     WWW    WWWWW           WWW          WWWWWW         I",
    "I___IGI___WGGC    GGG    GGGGG           GGG          GGGGGG         I",
    "IWWWGGGWWWGGGWWWWWGGGWWWWGGGGGWWWWWWWWWWWGGGWWWWWWWWWWGGGGGGWWWWWWWWWI",
    "IGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGI"
]
newLevel = level[::-1]
player = Actor("snok", (WIDTH / 2, (HEIGHT / 2)))
wall = Actor("ground", (WIDTH / 2, 500))

x = 0
y = 1

rx = 5
lx = 5


speed = 3

height = HEIGHT + 25

hitright = False
hitleft = False


class Ground(object):

    def __init__(self, pos):
        grounds.append(self)
        self.rect = Rect(pos[0], pos[1], 50, 1)


for row in newLevel:
    for col in row:
        if col == "W":
            walls.append(Actor("ground2", (50*x, height - (50 * y))))
        if col == "G":
            walls.append(Actor("ground3", (50*x, height - (50 * y))))
        if col == "I":
            stones.append(Actor("close", (50*x, height - (50 * y))))
        if col == "C":
            coins.append(Actor("coin", (50*x, height - (50 * y))))
        if col == "_":

            grounds.append(Actor("border", (50 * x, height - 47 * y)))
            #Ground((50 * x, height-(50 * y)))
        x += 1
    y += 1
    x = 0


def collision_stones():
    for stone in stones:
        if stone.colliderect(player):
            return True
    for wall in walls:
        if wall.colliderect(player):
            return True
    return False


def collision_ground():
    for ground in grounds:
        if ground.colliderect(player):
            return True
    return False


def draw():
    player.draw()
    for wall in walls:
        wall.draw()
    for stone in stones:
        stone.draw()
    for coin in coins:
        coin.draw()
    for ground in grounds:
        #screen.draw.rect(ground.rect, (0,0,255))
        ground.draw()
    global speed

    if not collision_ground():
        player.y += speed


####################################################################################
# Wenn ein Eckstein vorhanden ist und der Spieler nicht oben drauf steht muss er
# herunterfallen, sowie muss gegeben sein, dass der Spieler sich nicht durch den
# Stein bewegen kann.
# Nur wenn der Spieler oben auf dem Stein steht das sich seine y Koordinate nicht
# mehr nach unten bewegen
# Evt. über eine neuen Buchstaben und Funktion, wo überprüft wird ob der Spieler über
# dem neuen Buchstaben (Stein) ist ( player.botto und corner.top)
####################################################################################


def update():

    global lx
    global rx
    global hitright
    global hitleft
    screen.clear()

    print(hitright, hitleft)

    if keyboard.right:
        if not collision_stones():
            for stone in stones:
                stone.left -= rx
            for wall in walls:
                wall.left -= rx
            for coin in coins:
                coin.left -= rx
            for ground in grounds:
                ground.left -= rx
            hitright = False

        if collision_stones():
            hitright = True

        if collision_stones() and hitleft == True:
            for stone in stones:
                stone.left -= rx
            for wall in walls:
                wall.left -= rx
            for coin in coins:
                coin.left -= rx
            for ground in grounds:
                ground.left -= rx
            hitleft = False

    if keyboard.left:


        if not collision_stones():
            for stone in stones:
                stone.left += rx
            for wall in walls:
                wall.left += rx
            for coin in coins:
                coin.left += rx
            for ground in grounds:
                ground.left += rx
            hitleft = False

        if collision_stones():
            hitleft = True


        if collision_stones() and hitright == True:
            for stone in stones:
                stone.left += rx
            for wall in walls:
                wall.left += rx
            for coin in coins:
                coin.left += rx
            for ground in grounds:
                ground.left += rx
            hitright = False

    elif keyboard.up:
        if(player.y > 350):
            player.y -= 5


pgzrun.go()


# background = Actor("stage", (WIDTH / 2, HEIGHT / 2))

# x = 0
# y = 1

# height = HEIGHT + 25

# #player.vy = 1

# hit = False

# for row in newLevel:
#     for col in row:
#         if col == "W":
#             walls.append(Actor("ground2", (50*x, height - (50 * y))))
#         if col == "G":
#             walls.append(Actor("ground3", (50*x, height - (50 * y))))
#         if col == "I":
#             stones.append(Actor("close", (50*x, height - (50 * y))))
#         if col == "C":
#             coins.append(Actor("coin", (50*x, height - (50 * y))))
#         x += 1
#     y += 1
#     x = 0

# def move_level(dx):
#     for wall in walls:
#         wall.x -= dx

#     for coin in coins:
#         coin.x -= dx

#     for stone in stones:
#         stone.x -= dx

# def falling(vy):
#     player.y += vy

# def collision():
#     for wall in walls:
#         if player.colliderect(wall):
#             falling(0)

# def draw():
#     background.draw()
#     player.draw()

#     for wall in walls:
#         wall.draw()
#     for stone in stones:
#         stone.draw()
#     for coin in coins:
#         coin.draw()


# def update():
#     for wall in walls:
#         falling(1)

#         print(player.y)
#         if player.colliderect(wall):
#             falling(0)


#     if keyboard.right:
#         move_level(5)

#     if keyboard.left:
#         move_level(-5)


#     # for stone in stones:
#     #     if player.colliderect(stone):
#     #         player.vy = 0
#     #         player.y = wall.top
#     #         player.velocity = 0

#     # if keyboard.right:
#     #     for wall in walls:
#     #         wall.left -= 5
#     #     for stone in stones:
#     #         stone.left -= 5
#     #     for coin in coins:
#     #         coin.left -= 5

#     # if keyboard.left:
#     #     for wall in walls:
#     #         wall.left += 5
#     #     for stone in stones:
#     #         stone.left += 5
#     #     for coin in coins:
#     #         coin.left += 5

#     # if keyboard.up:
#     #     if jump == True:
#     #         player.vy = FLAP_VELOCITY
#     #         player.y -= 2
