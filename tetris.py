#tetris? oh boy here we go again. what is this? the 7th try??

from pprint import pprint as p
import random
import os
from pynput import keyboard
import time


#log = open("log.txt","a")

class Tetrinimo:

    shapes = [1,2,3,4,5,6,7]
    
    shapes[0] = [['-','-','*','-'],
                 ['-','-','*','-'],
                 ['-','-','*','-'],
                 ['-','-','*','-']]

    shapes[1] = [['-','-','-','-'],
                 ['-','*','*','-'],
                 ['-','*','*','-'],
                 ['-','-','-','-']]

    shapes[2] = [['-','-','-','-'],
                 ['-','*','*','*'],
                 ['-','-','*','-'],
                 ['-','-','-','-']]

    shapes[3] = [['-','-','*','-'],
                 ['-','*','*','-'],
                 ['-','*','-','-'],
                 ['-','-','-','-']]

    shapes[4] = [['-','*','-','-'],
                 ['-','*','*','-'],
                 ['-','-','*','-'],
                 ['-','-','-','-']]

    shapes[5] = [['-','*','*','-'],
                 ['-','-','*','-'],
                 ['-','-','*','-'],
                 ['-','-','-','-']]

    shapes[6] = [['-','*','*','-'],
                 ['-','*','-','-'],
                 ['-','*','-','-'],
                 ['-','-','-','-']]

    
    def __init__(self, shape, i, j):
        self.shape = shape
        self.i = i
        self.j = j
        self.blocks = Tetrinimo.shapes[shape]

    def rotate(self):
        g = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
        for i in range(4):
            for j in range(4):
                g[j][3-i] = self.blocks[i][j]

        #p(g)
        
        if not self.collision(g, self.i, self.j):
            #print("Here")
            #p(g)
            for i in range(4):
                for j in range(4):
                    self.blocks[i][j] = g[i][j]

            #p(self.blocks)
            
            self.place()
                
        
    def place(self):
        for i in range(24):
            for j in range(10):
                if board[i][j] == "*":
                    board[i][j] = " "
        
        for i in range(4):
            for j in range(4):
                if self.i+i < 24 and self.j + j < 10:
                    if self.blocks[i][j] == "*":
                        board[self.i+i][self.j+j] = self.blocks[i][j]
                
                
    def collision(self, g,si,sj):
        for i in range(4):
            for j in range(4):
                if g[i][j] == "*":
                    if i+si < 24 and j+sj < 10:
                        if board[i+si][j+sj] == "X":
                            return True
                    else:
                        if not i+si<24:
                            return True

        return False


##    def sideColl(self, g):
##        for i in range(4):
##            for j in range(4):
##                if g[i][j] == "*":
##                    if i+self.i < 24 and j+self.j < 10:
##                        if board[i][j+self.j]
    
    def moveDown(self):
        
        if not self.collision(self.blocks,self.i+1, self.j):
            self.i += 1
            self.place()
            return True
        else:
            print("Here")
            for i in range(24):
                for j in range(10):
                    if board[i][j] == "*":
                        board[i][j] = "X"

            return False

    def md(self):
        self.i += 1
        if not self.downColl(self.blocks):
            self.place()
            return True
        else:
            for i in range(24):
                for j in range(10):
                    if board[i][j] == "*":
                        board[i][j] = "X"
            return False
    
    def moveRight(self):
##        self.j += 1
        if not self.collision(self.blocks, self.i, self.j+1):
            self.j+=1
            self.place()

    def moveLeft(self):
##        self.j -= 1
        if not self.collision(self.blocks, self.i, self.j-1):
            self.j -= 1
            self.place()
    

def printBoard(board,lines):
    print(" -"*10)
    for i in range(24):
        for j in range(10):
            if j == 0:
                print("|", end = "")
            print(board[i][j], end = " ")
        print("|")
    print(" -"*10)
    print("LINES:", lines)

def clearLines(lines):
    for i in range(24):
        flag = True
        for j in range(10):
            if board[i][j] != "X":
                flag = False
        if flag:
            lines+=1
            for j in range(10):
                board[i][j] = " "
            for k in range(i,0,-1):
                for s in range(10):
                    #if board[k][s] == "X":
                    board[k][s] = board[k-1][s]
    return lines


board = [ [" " for i in range(10)] for i in range(24)]

shp  = random.randrange(7)

t = Tetrinimo(shp,0,4)
t.place()
'''
while True:
    os.system('cls')
    printBoard(board)
    if not t.moveDown():
        shp = random.randrange(7)
        t = Tetrinimo(shp,0,4)
        t.place()
    f = os.stdin(1)
    if f == "x":
        t.rotate()
        os.system('cls')
    if f == "j":
        t.moveLeft()
        os.system('cls')
    if f == "l":
        t.moveRight()
        os.system('cls')
    t.moveDown()
   '''

lines = 0

def on_press(key):
    global lines
    if str(key) == "Key.space":
        t.rotate()
        
    elif str(key) == "Key.left":
        t.moveLeft()
        
    elif str(key) == "Key.right":
        t.moveRight()
        
    elif str(key) == "Key.down":
        t.moveDown()
        
    
    os.system('cls')
    lines = clearLines(lines)
    printBoard(board, lines)


listener = keyboard.Listener(on_press = on_press)
listener.start()

while True:
    printBoard(board, lines)
   
    if not t.moveDown():
        shp = random.randrange(7)
        t = Tetrinimo(shp,0,4)
        t.place()
    time.sleep(0.25)
    os.system('cls')
    lines = clearLines(lines)

