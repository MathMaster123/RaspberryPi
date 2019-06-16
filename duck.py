from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
X = (0, 0, 0)
O = (0, 0, 0)
W = (255, 255, 255)
squares = [top_left(green), top_center(green), top_right(green), left_center(green), center(green), right_center(green), bottom_left(green), bottom_center(green), bottom_right(green)]
drawboard = [X, X, W, O, O, W, O, O,
             X, X, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,
             W, W, W, W, W, W, W, W,
             O, O, W, O, O, W, O, O,
             O, O, W, O, O, W, O, O,]
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
def toggle():
    for event in sense.stick.get_events():
        if event.action = "pressed" and event.direction == "right":
            squares[0]
sense.set_pixels(drawboard)
