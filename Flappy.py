from random import randint
from time import sleep
from sense_hat import SenseHat

sense = SenseHat()
x = 0
y = 0
red=(255, 0, 0)
yellow=(255, 255, 0)
blue=(0, 0, 255)

matrix = [[blue for column in range(8)] for row in range(8)]
def flatten(matrix):
	flattened = [pixel for row in matrix for pixel in row]
	return flattened
def draw_matrix(matrix):
  for row in matrix:
    row[-1] = red
  gap = randint(1, 6)
  matrix[gap][-1] = blue
  matrix[gap+1][-1] = blue
  matrix[gap-1][-1] = blue
  return matrix
def move_pipes(matrix):
  for row in matrix:
    for i in range(7): 
      row[i] = row[i+1]
    row[-1] = blue 
  return matrix
def draw_astronaut(event):
    global y
    global x
    sense.set_pixel(x, y, blue)
    if event.action == "pressed":
        if event.direction == "up" and y>0:
            y -= 1
        elif event.direction == "down" and y<7:
            y += 1
        elif event.direction == "right" and x<7:
            x += 1
        elif event.direction == "left" and x>0:
            x -= 1
    sense.set_pixel(x, y, yellow)    


sense.stick.direction_any = draw_astronaut

while True:
  matrix = draw_matrix(matrix)
  for i in range(3):
    sense.set_pixels(flatten(matrix))
    matrix = move_pipes(matrix)
    sleep(1)

