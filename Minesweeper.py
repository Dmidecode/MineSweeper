from case import Case
from utils import printPlateau, initPlateau, isGameOver, discoverPlateau, displayGameOver
import os


width = 8
height = 5
plateau = [[]] * height
lost = False
for y in range(height):
    plateau[y] = [] * width
    for x in range(width):
        plateau[y].append(Case())

initPlateau(plateau, width, height)
while not isGameOver(plateau, width, height):
    os.system('cls')
    printPlateau(plateau, width, height)
    print('Choisir un position (x, y)')
    print('X: ', end = '')
    xUser = int(input()) - 1
    print('Y: ', end = '')
    yUser = int(input()) - 1
    
    if plateau[yUser][xUser].isMine:
        plateau[yUser][xUser].open = True
        displayGameOver(plateau, width, height)
        lost = True
        break

    discoverPlateau(plateau, width, height, xUser, yUser)

if not lost:
    os.system('cls')
    printPlateau(plateau, width, height)
    print('GG WP')
