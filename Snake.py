from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()
dead = False
pause = .5
snake = [[2, 4], [3, 4], [4, 4]]
white = (255, 255, 255)
green = (0, 255, 0)
blank = (0, 0, 0)
score = 0
direction = "right"
veggies = []
def make_veg():
    x = randint(0, 7)
    y = randint(0, 7)
    veg = [x, y]
    while veg in snake:
        x = randint(0, 7)
        y = randint(0, 7)
        veg = [x, y]
    sense.set_pixel(veg[0], veg[1], green)
    veggies.append(veg)
def joystick_moved(event):
    global direction
    direction = event.direction
def wrap(pix):
    if pix[0] > 7:
        pix[0] = 0
    if pix[0] < 0:
        pix[0] = 7
    if pix[1] < 0:
        pix[1] = 7
    if pix[1] > 7:
        pix[1] = 0

    return pix
def move():
  global pause
  remove = True
  last = snake[-1]
  first = snake[0]
  next = list(last)  
  if direction == "right":
    next[0] = last[0] + 1
  if direction == "left":
    next[0] = last[0] - 1
  if direction == "down":
    next[1] = last[1] + 1
  if direction == "up":
    next[1] = last[1] - 1
  if next in snake:
      dead = True
  snake.append(next)
  wrap(next)
  sense.set_pixel(next[0], next[1], white)
  if next in veggies:
    veggies.remove(next)
    global score
    score+=1
    if score%5 == 0:
      remove = False
      pause *= .8
  if remove == True:
    sense.set_pixel(first[0], first[1], blank)
    snake.remove(first)
def draw_snake():
    for segment in snake:
        sense.set_pixel(segment[0], segment[1], white)
sense.clear()
while dead == False:
  sense.stick.direction_any = joystick_moved
  draw_snake()
  move()
  if len(veggies) < 3 and randint(1, 5) > 4:
    make_veg()
  sleep(pause)
sense.show_message("You got " + score + " points!")

