import pgzrun
import pygame
import time
import numpy

WIDTH = 1200
HEIGHT = 700
GRAVITY = 0.4
FLAP_VELOCITY = -10.5

walls = []
stones = []
coins = []

level = [
    "I                                    CCC                             I",
    "I                                  WWWWWW                            I",
    "I                               WWWGGGGGG                            I",
    "I                 WWWWWW    WWWWGGGGGGGGG                            I",
    "I                 GGGG                                               I",
    "I              W                                                     I",
    "I            WWG                                                     I",
    "I          WWGGG                                                     I",
    "I   WWW    GG     WWW    WWWWW           WWW          WWWWWW         I",
    "I   GGG   WGGC    GGG    GGGGG           GGG          GGGGGG         I",
    "IWWWGGGWWWGGGWWWWWGGGWWWWGGGGGWWWWWWWWWWWGGGWWWWWWWWWWGGGGGGWWWWWWWWWI",
    "IGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGI"
]

newLevel = level[::-1]

player = Actor("snok", (WIDTH / 2, (HEIGHT / 2)))
background = Actor("stage", (WIDTH / 2, HEIGHT / 2))

x = 0
y = 1

height = HEIGHT + 25

player.vy = 0

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
        x += 1
    y += 1
    x = 0


def update_player():
    player.vy += GRAVITY
    player.y += player.vy
    player.x = 100
    print("Player vy: " + str(player.vy) + " Player y: " + str(player.y))


def draw():
    background.draw()
    player.draw()
    for wall in walls:
        wall.draw()
    for stone in stones:
        stone.draw()
    for coin in coins:
        coin.draw()


def update():
    screen.clear()
    global jump
    jump = False
    update_player();


    for wall in walls:
        if player.colliderect(wall):
            # print(player.colliderect(wall))
            jump = True
            GRAVITY = 0;
            player.vy = 0                 
            player.y = wall.top - 10
            player.velocity = 0
            player.vy = 0;
        else:
            jump = False
    for stone in stones:
        if player.colliderect(stone):
            player.vy = 0
            player.y = wall.top
            player.velocity = 0

    if keyboard.right:
        for wall in walls:
            wall.left -= 5
        for stone in stones:
            stone.left -= 5
        for coin in coins:
            coin.left -= 5

    if keyboard.left:
        for wall in walls:
            wall.left += 5
        for stone in stones:
            stone.left += 5
        for coin in coins:
            coin.left += 5

    if keyboard.up:
        if jump == True:
            player.vy = FLAP_VELOCITY
            player.y -= 2


pgzrun.go()
