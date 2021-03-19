##set up basic rules for 2048
##maby look at montecarlo search algo
##take specified length of posible states as input
##output which key to press

import random
from prettytable import PrettyTable

class board():
    def __init__(self):
        self.values =  [[0, 0, 0, 0], 
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
    def start(self):
        startingX = random.randint(0, 3)
        startingY = random.randint(0, 3)
        self.values[startingX][startingY] = 2
    
    def print(self):
        Table = PrettyTable()
        for x in range(4):
            Table.add_row([self.values[x][0], self.values[x][1], self.values[x][2], self.values[x][3]])
        print(Table)        


                # val = self.values[x][i]
                # if len(str(self.values[x][i])) % 2 == 1:
                #     spaceLength = int((len(str(self.values[x][i]))-1)/2)
                # else:
                #     spaceLength = int((len(str(self.values[x][i])))/2)
                # numString = "|"
                # for n in range(spaceLength):
                #     numString = numString + " "
                # numString = numString + str(val)
                # for n in range(spaceLength):
                #     numString = numString + " "
                # numString = numString + "|"
                # print(numString)
                # print("+----------+")


    def moveUp(self):
        for j in range(3):
            for x in range(3):
                for i in range(4):
                    if self.values[x][i] == 0:
                        self.values[x][i] = self.values[x+1][i]
                        self.values[x+1][i] = 0


        for x in range(3):
            for i in range(4):
                if self.values[x+1][i] == self.values[x][i]:
                    self.values[x+1][i] = 0
                    self.values[x][i] += self.values[x][i]

        for x in range(3):
            for i in range(4):
                if self.values[x][i] == 0:
                        self.values[x][i] = self.values[x+1][i]
                        self.values[x+1][i] = 0


            
        

mainBoard = board()
mainBoard.start()
mainBoard.print()
mainBoard.moveUp()
mainBoard.print()
