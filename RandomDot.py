from sense_hat import SenseHat
from random import randint
import time
sense = SenseHat()

O = [0, 0, 0]
for num in range(0, 5):
  colour_1=randint(0, 255)
  colour_2=randint(0, 255)
  colour_3=randint(0, 255)
  X = [colour_1, colour_2, colour_3]
  dot = [
  O, O, O, O, O, O, O, O,
  O, O, O, X, X, O, O, O,
  O, O, X, X, X, X, O, O,
  O, X, X, X, X, X, X, O,
  O, X, X, X ,X ,X ,X ,O,
  O, O, X, X, X, X, O, O,
  O, O, O, X, X, O, O, O,
  O, O, O, O, O, O, O, O
  ]
  sense.set_pixels(dot)
  time.sleep(1)
  sense.clear()
  time.sleep(1)
sense.show_message("IT WORKED! YOU DID IT!!")
