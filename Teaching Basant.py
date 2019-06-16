from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()
red = [255, 0, 0]
def dropChip(col, p):
    global board
    row=0
         
    while board[col][row] == '':
        if row == 7 or board[col][row+1] != '':
            board[col][row] = p
            return row
         
        sense.set_pixel(col, row, 0,0,0)
        row += 1
        sense.set_pixel(col, row, p[0], p[1], p[2])
        time.sleep(0.1)
def checkWin(p, c, r):
    global board
    ### check horizontal    
    leftCount = countAdjacent(p, c, r, 0, -1)
    rightCount = countAdjacent(p, c, r, 0, 1)
    totalCount = 1 + leftCount + rightCount
 
    if totalCount >= 4:
        sense.show_message("Game Over!")
 
    ### check top left to bottom right
    leftCount = countAdjacent(p, c, r, -1, -1)
    rightCount = countAdjacent(p, c, r, 1, 1)
    totalCount = 1 + leftCount + rightCount
 
    if totalCount >= 4:
        sense.show_message("Game Over!")
 
    ### check for bottom left to top right
    leftCount = countAdjacent(p, c, r, 1, -1)
    rightCount = countAdjacent(p, c, r, -1, 1)
    totalCount = 1 + leftCount + rightCount
 
    if totalCount >= 4:
        sense.show_message("Game Over!")
 
    ### check verticle
    downCount = countAdjacent(p, c, r, 1, 0)
    totalCount = 1 + downCount
 
    if totalCount >= 4:
        sense.show_message("Game Over!")
 
    return False
 
###------------------------------------------------------
### countAdjacent takes a column change (yChange)
###   and rowChange (xChange) and returns the number  
###   of adjacent chips in that direction from the original spot
###------------------------------------------------------    
def countAdjacent(p, c, r, yChange, xChange):
    global board
    adjacentCount = 0
    while True :
        c = c + xChange
        if c < 0 or c > 7:
            return adjacentCount
         
        r = r + yChange
        if r < 0 or r > 7:
            return adjacentCount
         
        if board[r] == p:
            adjacentCount = adjacentCount + 1
        else:
            return adjacentCount
def getMove(p) :
    currentColumn = 0
    sense.set_pixel(currentColumn,0, p[0], p[1], p[2]) 
 
    while True:
        for event in sense.stick.get_events():
            if event.action == "pressed":
                if event.direction == "right":
                    if currentColumn < 7:                        
                        sense.set_pixel(currentColumn, 0, 0,0,0) ## turn off LED where chip was                       
                        currentColumn += 1
                        sense.set_pixel(currentColumn, 0, p[0], p[1], p[2])  ## light up new spot where chip is with color of player (p)
                if event.direction == "left":
                    if currentColumn > 0:
                        sense.set_pixel(currentColumn, 0, 0,0,0)  ## turn off LED where chip was  
                        currentColumn -= 1
                        sense.set_pixel(currentColumn, 0, p[0], p[1], p[2]) ## light up new spot where chip is with color of player (p)
                if event.direction == "down":
                    False
                    return currentColumn
RED = [255,0,0]
BLUE = [0,0,255]
player = RED
board = [
          [ '', '', '', '', '', '', '', ''],
          [ '', '', '', '', '', '', '', ''],
          [ '', '', '', '', '', '', '', ''],
          [ '', '', '', '', '', '', '', ''],
          [ '', '', '', '', '', '', '', ''],
          [ '', '', '', '', '', '', '', ''],
          [ '', '', '', '', '', '', '', ''],
          [ '', '', '', '', '', '', '', '']
]
win = False
while True:
    selectedColumn = getMove(player)
    dropChip(selectedColumn, player)
    if (player == RED):
        player= BLUE
    else:
        player = RED
