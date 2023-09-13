from object import object
from planetsystem import planetsystem
import pygame
import math
ZM = 1.9885*10**30
AU = 149597870700
h = 100
# object1 = object(1*ZM, [0,0], [0,0])
# object2 = object(1/102970.52913596784*ZM, [149597870700,0], [0,29780])
# object3 = object(1/27061785.519869354*ZM, [151597870700,0], [0,29000])

solarsystem = planetsystem()
with open('config.txt') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if i == 0:
        h = int(lines[i])
    elif i == 1:
        realsize = eval(lines[i])
    else:
        try:
            solarsystem.objects.append(eval("object("+lines[i]+")"))
        except:
            print("kon lijn " + str(i+1) + " niet lezen, dit object is overgeslagen")
            print("een lijn hoord te bestaan uit mass(float), positie(tuple of lijst), snelheid(tuple of lijst)")

pygame.init()


# Colours
BACKGROUND = (0, 0, 0)

SIZE = 1000
resize =SIZE/4
# Game Setup
WINDOW_WIDTH = SIZE
WINDOW_HEIGHT = SIZE
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


#The main function that controls the game
def main():
    looping = True
    zoom = 1
    upmod = 0
    rightmod = 0
    speed = 0.01
    # The main game loop
    while looping:
        #pygame.time.delay(10)
        # Get inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                looping = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    zoom += 1
                elif event.key == pygame.K_c:
                    if zoom > 1:
                        zoom -= 1
                elif event.key == pygame.K_z:
                    upmod += speed
                elif event.key == pygame.K_q:
                    rightmod -= speed
                elif event.key == pygame.K_s:
                    upmod -= speed
                elif event.key == pygame.K_d:
                    rightmod += speed
            # [...]


        WINDOW.fill(BACKGROUND)
        drawdata = solarsystem.drawData()
        for data in drawdata:
            s  = math.log(data[2]*10)
            if s < 1:
                s = 1
            pygame.draw.circle(WINDOW, (255,255,255), (SIZE*(1/2- rightmod + data[0]*2/realsize*(0.25*zoom)), SIZE*(1/2+ upmod + data[1]*2/realsize*(0.25*zoom))), 1 )

        solarsystem.step(h)

        # Render elements of the game

        pygame.display.update()


main()



