import random
import os

def displayGameOver(plateau, width, height):
    os.system('cls')
    print('Tombe sur une mine !')
    printPlateau(plateau, width, height)

def discoverPlateau(plateau, width, height, x, y):
    plateau[y][x].open = True
    if numberMineAround(plateau, width, height, x, y) == 0:
        yMin = max(y - 1, 0)
        yMax = min(y + 2, height)
        xMin = max(x - 1, 0)
        xMax = min(x + 2, width)
        for posY in range(yMin, yMax):
            for posX in range(xMin, xMax):
                if plateau[posY][posX].open:
                    continue
                discoverPlateau(plateau, width, height, posX, posY)
    return False

def isGameOver(plateau, width, height):
    for y in range(height):
        for x in range(width):
            if plateau[y][x].isMine and plateau[y][x].open:
                return True
            if not plateau[y][x].isMine and not plateau[y][x].open:
                return False
    return True

def initPlateau(plateau, width, height):
    for y in range(height):
        for x in range(width):
            percentMine = random.random() < 0.2
            plateau[y][x].isMine = bool(percentMine)

def numberMineAround(plateau, width, height, x, y):
    res = 0
    yMin = max(y - 1, 0)
    yMax = min(y + 2, height)
    xMin = max(x - 1, 0)
    xMax = min(x + 2, width)

    for posY in range(yMin, yMax):
        for posX in range(xMin, xMax):
            if posX == x and posY == y:
                continue
            if plateau[posY][posX].isMine:
                res += 1

    return res

def printPlateau(plateau, width, height):
    print('    ', end = '')
    for x in range(width):
        print(f'{x + 1} | ', end = '')
    print()
    for y in range(height):
        print(f'{y + 1} | ', end = '')
        for x in range(width):
            casePlateau = plateau[y][x]
            displayCase = 'x'
            if casePlateau.open:
                if casePlateau.isMine:
                    displayCase = '!'
                else:
                    displayCase = numberMineAround(plateau, width, height, x, y)
            print(f'{displayCase} | ', end = '')
        print()




