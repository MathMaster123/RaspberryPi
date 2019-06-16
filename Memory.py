from sense_hat import SenseHat
from time import sleep
from random import randint
from random import shuffle
sense = SenseHat()
red = (255, 0, 0)
orange = (255, 128, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (153, 0, 153)
pink = (255, 102, 178)
dark_green = (76, 153, 0)
white = (255, 255, 255)
color_list = [red, orange, yellow, green, blue, purple, pink, dark_green]
shuffle(color_list)
sense.clear()
color = white
inlist = 0
current_pixel = [0, 0]
while True:
  for event in sense.stick.get_events():
    if event.direction == "right" and event.action == "pressed":
      sense.set_pixel(current_pixel[0], current_pixel[1], 0, 0, 0)
      if current_pixel[0]<7:
        current_pixel[0]+=1
        inlist+=1
    if event.direction == "left" and event.action == "pressed":
      sense.set_pixel(current_pixel[0], current_pixel[1], 0, 0, 0)
      if current_pixel[0]>0:
        current_pixel[0]-=1
        inlist-=1
    if event.direction == "down" and event.action == "pressed":
      sense.set_pixel(current_pixel[0], current_pixel[1], 0, 0, 0)
      if current_pixel[1]<7:
        current_pixel[1]+=1
        inlist+=8
    if event.direction == "up" and event.action == "pressed":
      sense.set_pixel(current_pixel[0], current_pixel[1], 0, 0, 0)
      if current_pixel[1]>0:
        current_pixel[1]-=1
        inlist-=8
    if event.direction == "middle" and event.action == "pressed":
      sense.set_pixel(current_pixel[0], current_pixel[1], color_list[inlist])
      sleep(.5)
  sense.set_pixel(current_pixel[0], current_pixel[1], color)
  

