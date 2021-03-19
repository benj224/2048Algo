##set up basic rules for 2048
##maby look at montecarlo search algo
##take specified length of posible states as input
##output which key to press

import random

class board():
    def __init__(self):
        self.values =  [[0, 0, 0, 0], 
                        [0, 0, 0, 0],
                        [0, 0, 0, 0],
                        [0, 0, 0, 0]]
    def start():
        startingX = random.randint(4)
        startingY = random.randint(4)
        self.values[startingX][startingY] = 2
        


