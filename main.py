__author__ = 'grahamhub'

import time
import random


def starting():
    print('Starting program...')
    time.sleep(1)
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)


# starting the game
def rules():
    print('Here are the rules:')
    print('1) You want your color to dominate the board.')
    print('2) Take over opponent tiles by sandwiching them between your tiles(Vertically/Horizontally).')
    print('3) You can only place a tile next to one already on the board.')
    print('4) When choosing a tile, please use the syntax X1. Ex: A4, F7, B1.')
    print('5) If it is two player, turns will switch with every round.')


def startup():
    gamemode = input('One or two players? ')
    if gamemode == 'two' or gamemode == 'Two' or gamemode == '2':
        return True
    elif gamemode == 'one' or gamemode == 'One' or gamemode == '1':
        return False


def difficulty():
    diff = input('Easy or hard mode? ')
    if diff == 'easy' or diff == 'Easy':
        return True
    elif diff == 'hard' or diff == 'Hard':
        return False


# choosing a space
def choosetile():
    playerinput = list(input('Choose a tile(P1): '))
    first = playerinput[0]
    second = playerinput[1]
    if first == 'A' or first == 'B' or first == 'C' or first == 'D' or first == 'E' or first == 'F' or first == 'G' or first == 'H':
        if second == '1' or second == '2' or second == '3' or second == '4' or second == '5' or second == '6' or second == '7' or second == '8':
            return True
    else:
        print('Wrong syntax: letter must be capital')
        return False


def choosetilep2():
    playerinput = list(input('Choose a tile(P2): '))
    first = playerinput[0]
    second = playerinput[1]
    if first == 'A' or first == 'B' or first == 'C' or first == 'D' or first == 'E' or first == 'F' or first == 'G' or first == 'H':
        if second == '1' or second == '2' or second == '3' or second == '4' or second == '5' or second == '6' or second == '7' or second == '8':
            return True
    else:
        print('Wrong syntax: letter must be capital')
        return False


# gameboard
def printboard():
    gameboard = open('OthelloPYC', 'r+')
    print(gameboard.read())
    z = 1
    for x in range(0, 8):
        print((z), (' ' + boardArray[x][0] + '   ' + boardArray[x][1] + '   ' + boardArray[x][2] + '   ' + boardArray[x][
            3] + '   ' +
                   boardArray[x][4] + '   ' + boardArray[x][5] + '   ' + boardArray[x][6] + '   ' + boardArray[x][7]))
        z += 1


# changing a tile
def chartonum(column):
    if column == 'A':
        return 0
    elif column == 'B':
        return 1
    elif column == 'C':
        return 2
    elif column == 'D':
        return 3
    elif column == 'E':
        return 4
    elif column == 'F':
        return 5
    elif column == 'G':
        return 6
    elif column == 'H':
        return 7


def checkboard(x, y):
    # x + 1 down, y + 1 right, x - 1 up, y - 1 left
    w = 1
    z = 2
    cp = boardArray[x][y]
    if cp == 'W':
        op = 'B'
    elif cp == 'B':
        op = 'W'
    if y == 7 and x != 7:
        while boardArray[x + w][y] == op:
            if boardArray[x + z][y] == cp:
                boardArray[x + w][y] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x + z][y] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x - w][y] == op:
            if boardArray[x - z][y] == cp:
                boardArray[x - w][y] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x - z][y] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x][y - w] == op:
            if boardArray[x][y - z] == cp:
                boardArray[x][y - w] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x][y - z] == op:
                w += 1
                z += 1
            else:
                break
    elif x == 7 and y != 7:
        while boardArray[x - w][y] == op:
            if boardArray[x - z][y] == cp:
                boardArray[x - w][y] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x - z][y] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x][y - w] == op:
            if boardArray[x][y - z] == cp:
                boardArray[x][y - w] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x][y - z] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x][y + w] == op:
            if boardArray[x][y + z] == cp:
                boardArray[x][y + w] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x][y + z] == op:
                w += 1
                z += 1
            else:
                break
    elif x == 7 and y == 7:
        while boardArray[x - w][y] == op:
            if boardArray[x - z][y] == cp:
                boardArray[x - w][y] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x - z][y] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x][y - w] == op:
            if boardArray[x][y - z] == cp:
                boardArray[x][y - w] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x][y - z] == op:
                w += 1
                z += 1
            else:
                break
    else:
        while boardArray[x + w][y] == op:
            if boardArray[x + z][y] == cp:
                boardArray[x + w][y] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x + z][y] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x - w][y] == op:
            if boardArray[x - z][y] == cp:
                boardArray[x - w][y] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x - z][y] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x][y - w] == op:
            if boardArray[x][y - z] == cp:
                boardArray[x][y - w] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x][y - z] == op:
                w += 1
                z += 1
            else:
                w = 1
                z = 2
                break
        while boardArray[x][y + w] == op:
            if boardArray[x][y + z] == cp:
                boardArray[x][y + w] = cp
                if w > 0:
                    w -= 1
            elif boardArray[x][y + z] == op:
                w += 1
                z += 1
            else:
                break


def tilechangep1():
    playerchoice = list(input('Please confirm choice: '))
    y = chartonum(playerchoice[0])
    x = int(playerchoice[1]) - 1
    if y == 0:
        boardArray[x][y] = p1
        checkboard(x, y)
    elif y == 1:
        boardArray[x][y] = p1
        checkboard(x, y)
    elif y == 2:
        boardArray[x][y] = p1
        checkboard(x, y)
    elif y == 3:
        boardArray[x][y] = p1
        checkboard(x, y)
    elif y == 4:
        boardArray[x][y] = p1
        checkboard(x, y)
    elif y == 5:
        boardArray[x][y] = p1
        checkboard(x, y)
    elif y == 6:
        boardArray[x][y] = p1
        checkboard(x, y)
    elif y == 7:
        boardArray[x][y] = p1
        checkboard(x, y)


def tilechangep2():
    playerchoice = list(input('Please confirm choice: '))
    y = chartonum(playerchoice[0])
    x = int(playerchoice[1]) - 1
    if y == 0:
        boardArray[x][y] = p2
        checkboard(x, y)
    elif y == 1:
        boardArray[x][y] = p2
        checkboard(x, y)
    elif y == 2:
        boardArray[x][y] = p2
        checkboard(x, y)
    elif y == 3:
        boardArray[x][y] = p2
        checkboard(x, y)
    elif y == 4:
        boardArray[x][y] = p2
        checkboard(x, y)
    elif y == 5:
        boardArray[x][y] = p2
        checkboard(x, y)
    elif y == 6:
        boardArray[x][y] = p2
        checkboard(x, y)
    elif y == 7:
        boardArray[x][y] = p2
        checkboard(x, y)


# checking for a winner
def checkforwinner():
    if boardArray[0].count('/') == 0:
        if boardArray[1].count('/') == 0:
            if boardArray[2].count('/') == 0:
                if boardArray[3].count('/') == 0:
                    if boardArray[4].count('/') == 0:
                        if boardArray[5].count('/') == 0:
                            if boardArray[6].count('/') == 0:
                                if boardArray[7].count('/') == 0:
                                    for x in range(0, 7):
                                        white = boardArray[x].count('W')
                                        black = boardArray[x].count('B')
                                        if white > black:
                                            return True
                                        elif white < black:
                                            return False


# computer
def comp_column():
    compcolumn = random.randint(0, 7)
    if compcolumn == 0:
        return 0
    elif compcolumn == 1:
        return 1
    elif compcolumn == 2:
        return 2
    elif compcolumn == 3:
        return 3
    elif compcolumn == 4:
        return 4
    elif compcolumn == 5:
        return 5
    elif compcolumn == 6:
        return 6
    elif compcolumn == 7:
        return 7


def comp_row():
    comprow = random.randint(0, 7)
    if comprow == 0:
        return 0
    elif comprow == 1:
        return 1
    elif comprow == 2:
        return 2
    elif comprow == 3:
        return 3
    elif comprow == 4:
        return 4
    elif comprow == 5:
        return 5
    elif comprow == 6:
        return 6
    elif comprow == 7:
        return 7


def computerconfirm_easy(y, x):
    while True:
        w = 1
        if y == 7 and x != 7:
            if boardArray[x + w][y] == p1:
                return True
            elif boardArray[x - w][y] == p1:
                return True
            elif boardArray[x][y - w] == p1:
                return True
            else:
                return False
        elif x == 7 and y != 7:
            if boardArray[x][y + w] == p1:
                return True
            elif boardArray[x - w][y] == p1:
                return True
            elif boardArray[x][y - w] == p1:
                return True
            else:
                return False
        elif x == 7 and y == 7:
            if boardArray[x - w][y] == p1:
                return True
            elif boardArray[x][y - w] == p1:
                return True
            else:
                return False
        else:
            if boardArray[x + w][y] == p1:
                return True
            elif boardArray[x - w][y] == p1:
                return True
            elif boardArray[x][y - w] == p1:
                return True
            if boardArray[x][y + w] == p1:
                return True
            else:
                return False


def computerchoice_easy():
    while True:
        y = comp_row()
        x = comp_column()
        go = computerconfirm_easy(y, x)
        if go is True:
            if boardArray[x][y] != p1 and boardArray[x][y] != p2:
                boardArray[x][y] = p2
                checkboard(x, y)
                break


def computerconfirm_hard(y, x):
    if computerconfirm_easy(y, x) is True:
        while True:
            w = 2
            if y == 7 and x != 7:
                if boardArray[x + w][y] == p2:
                    return True
                elif boardArray[x - w][y] == p2:
                    return True
                elif boardArray[x][y - w] == p2:
                    return True
                else:
                    return False
            elif x == 7 and y != 7:
                if boardArray[x][y + w] == p2:
                    return True
                elif boardArray[x - w][y] == p2:
                    return True
                elif boardArray[x][y - w] == p2:
                    return True
                else:
                    return False
            elif x == 7 and y == 7:
                if boardArray[x - w][y] == p2:
                    return True
                elif boardArray[x][y - w] == p2:
                    return True
                else:
                    return False
            else:
                if boardArray[x + w][y] == p2:
                    return True
                elif boardArray[x - w][y] == p2:
                    return True
                elif boardArray[x][y - w] == p2:
                    return True
                if boardArray[x][y + w] == p2:
                    return True
                else:
                    return False


def computerchoice_hard():
    while True:
        y = comp_row()
        x = comp_column()
        go_hard = computerconfirm_hard(y, x)
        if go_hard is True:
            if boardArray[x][y] != p1 and boardArray[x][y] != p2:
                boardArray[x][y] = p2
                checkboard(x, y)
                break


def compchoose():
    print('Computer choosing...')
    time.sleep(3)


starting()
rules()
boardArray = []
for x in range(0, 8):
    boardArray.append([])
    boardArray[x].append('/')
    boardArray[x].append('/')
    boardArray[x].append('/')
    boardArray[x].append('/')
    boardArray[x].append('/')
    boardArray[x].append('/')
    boardArray[x].append('/')
    boardArray[x].append('/')
boardArray[3][3] = 'W'
boardArray[3][4] = 'B'
boardArray[4][3] = 'B'
boardArray[4][4] = 'W'

if startup() is True:
    pL = input('Do you want to be white or black?(P1) ')
    if pL == 'w' or pL == 'W' or pL == 'white' or pL == 'White':
        p1 = 'W'
        p2 = 'B'
    elif pL == 'b' or pL == 'B' or pL == 'black' or pL == 'Black':
        p1 = 'B'
        p2 = 'W'
    while True:
        printboard()
        choosetile()
        tilechangep1()
        printboard()
        choosetilep2()
        tilechangep2()
        if checkforwinner() is True:
            print('White Wins!')
            break
        elif checkforwinner() is False:
            print('Black Wins!')
            break
else:
    pL = input('Do you want to be white or black? ')
    if pL == 'w' or pL == 'W' or pL == 'white' or pL == 'White':
        p1 = 'W'
        p2 = 'B'
    elif pL == 'b' or pL == 'B' or pL == 'black' or pL == 'Black':
        p1 = 'B'
        p2 = 'W'
    if difficulty() is True:
        while True:
            printboard()
            choosetile()
            tilechangep1()
            printboard()
            compchoose()
            computerchoice_easy()
            if checkforwinner() is True:
                print('White Wins!')
                break
            elif checkforwinner() is False:
                print('Black Wins!')
                break
    else:
        while True:
            printboard()
            choosetile()
            tilechangep1()
            printboard()
            compchoose()
            computerchoice_hard()
            if checkforwinner() is True:
                print('White Wins!')
                break
            elif checkforwinner() is False:
                print('Black Wins!')
                break
