from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
X = (0, 0, 0)
O = (0, 0, 0)
W = (255, 255, 255)
x=0
green = (0, 255, 0)
drawboard_OG=[O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O]
drawboard =  [O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O]
list_board = [("", "", ""),
              ("", "", ""),
             ("", "", "")]
def top_left(color):
    sense.set_pixel(0, 0, color)
    sense.set_pixel(0, 1, color)
    sense.set_pixel(1, 0, color)
    sense.set_pixel(1, 1, color)
def top_center(color):
    sense.set_pixel(3, 0, color)
    sense.set_pixel(3, 1, color)
    sense.set_pixel(4, 0, color)
    sense.set_pixel(4, 1, color)
def top_right(color):
    sense.set_pixel(6, 0, color)
    sense.set_pixel(6, 1, color)
    sense.set_pixel(7, 0, color)
    sense.set_pixel(7, 1, color)
def left_center(color):
    sense.set_pixel(0, 3, color)
    sense.set_pixel(0, 4, color)
    sense.set_pixel(1, 3, color)
    sense.set_pixel(1, 4, color)
def center(color):
    sense.set_pixel(3, 3, color)
    sense.set_pixel(4, 4, color)
    sense.set_pixel(3, 4, color)
    sense.set_pixel(4, 3, color)
def right_center(color):
    sense.set_pixel(6, 3, color)
    sense.set_pixel(6, 4, color)
    sense.set_pixel(7, 3, color)
    sense.set_pixel(7, 4, color)
def bottom_left(color):
    sense.set_pixel(0, 6, color)
    sense.set_pixel(0, 7, color)
    sense.set_pixel(1, 7, color)
    sense.set_pixel(1, 6, color)
def bottom_center(color):
    sense.set_pixel(3, 6, color)
    sense.set_pixel(4, 7, color)
    sense.set_pixel(3, 7, color)
    sense.set_pixel(4, 6, color)
def bottom_right(color):
    sense.set_pixel(6, 6, color)
    sense.set_pixel(6, 7, color)
    sense.set_pixel(7, 7, color)
    sense.set_pixel(7, 6, color)
squares = ["V", "V", "V", "V", "V", "V", "V", "V", "V"]

def toggle():
    global x
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "down":
            y=x%9-1
            squares[y] = "O"
            print(squares)
        if event.action == "pressed" and event.direction == "right":
            x+=1
        if event.action == "pressed" and event.direction == "left":
            x-=1
        if x%9 == 1:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            top_left(green)
          else:
            continue
            
        
        if x%9 == 2:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            top_center(green)
          else:
            continue
        if x%9 == 3:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            top_right(green)
          else:
            continue
        if x%9 == 4:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            left_center(green)
          else:
            continue
        if x%9 == 5:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            center(green)
          else:
            continue
        if x%9 == 6:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            right_center(green)
          else:
            continue
        if x%9 == 7:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            bottom_left(green)
          else:
            continue
        if x%9 == 8:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            bottom_center(green)
          else:
            continue
        if x%9 == 0:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            bottom_right(green)
          else:
            continue
         
sense.set_pixels(drawboard)
while True:
    toggle()
from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
X = (0, 0, 0)
O = (0, 0, 0)
W = (255, 255, 255)
x=0
green = (0, 255, 0)
drawboard_OG=[O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O]
drawboard =  [O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O]
list_board = [("", "", ""),
              ("", "", ""),
             ("", "", "")]
def top_left(color):
    sense.set_pixel(0, 0, color)
    sense.set_pixel(0, 1, color)
    sense.set_pixel(1, 0, color)
    sense.set_pixel(1, 1, color)
def top_center(color):
    sense.set_pixel(3, 0, color)
    sense.set_pixel(3, 1, color)
    sense.set_pixel(4, 0, color)
    sense.set_pixel(4, 1, color)
def top_right(color):
    sense.set_pixel(6, 0, color)
    sense.set_pixel(6, 1, color)
    sense.set_pixel(7, 0, color)
    sense.set_pixel(7, 1, color)
def left_center(color):
    sense.set_pixel(0, 3, color)
    sense.set_pixel(0, 4, color)
    sense.set_pixel(1, 3, color)
    sense.set_pixel(1, 4, color)
def center(color):
    sense.set_pixel(3, 3, color)
    sense.set_pixel(4, 4, color)
    sense.set_pixel(3, 4, color)
    sense.set_pixel(4, 3, color)
def right_center(color):
    sense.set_pixel(6, 3, color)
    sense.set_pixel(6, 4, color)
    sense.set_pixel(7, 3, color)
    sense.set_pixel(7, 4, color)
def bottom_left(color):
    sense.set_pixel(0, 6, color)
    sense.set_pixel(0, 7, color)
    sense.set_pixel(1, 7, color)
    sense.set_pixel(1, 6, color)
def bottom_center(color):
    sense.set_pixel(3, 6, color)
    sense.set_pixel(4, 7, color)
    sense.set_pixel(3, 7, color)
    sense.set_pixel(4, 6, color)
def bottom_right(color):
    sense.set_pixel(6, 6, color)
    sense.set_pixel(6, 7, color)
    sense.set_pixel(7, 7, color)
    sense.set_pixel(7, 6, color)
squares = ["V", "V", "V", "V", "V", "V", "V", "V", "V"]

def toggle():
    global x
    for event in sense.stick.get_events():
        if event.action == "pressed" and event.direction == "down":
            y=x%9-1
            squares[y] = "O"
            print(squares)
        if event.action == "pressed" and event.direction == "right":
            a=x+1
            if squares[a] = "V":
              x+=1
            else:
              x+=2
        if event.action == "pressed" and event.direction == "left":
            x-=1
        if x%9 == 1:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            top_left(green)
          else:
            continue
            
        
        if x%9 == 2:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            top_center(green)
          else:
            continue
        if x%9 == 3:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            top_right(green)
          else:
            continue
        if x%9 == 4:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            left_center(green)
          else:
            continue
        if x%9 == 5:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            center(green)
          else:
            continue
        if x%9 == 6:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            right_center(green)
          else:
            continue
        if x%9 == 7:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            bottom_left(green)
          else:
            continue
        if x%9 == 8:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            bottom_center(green)
          else:
            continue
        if x%9 == 0:
          if squares[0] == "V":
            sense.set_pixels(drawboard_OG)
            bottom_right(green)
          else:
            continue
         
sense.set_pixels(drawboard)
while True:
    sense.set_pixels(drawboard)
    toggle()
