import time
from sense_hat import SenseHat
sense = SenseHat()
green=(0, 0, 255)
X=[0, 0, 255]
O=[0, 0, 0]
HELLO = [
O, X, O, O, X, O, O, O,
O, X, O, O, X, O, X, O, 
O, X, O, O, X, O, O, O, 
O, X, X, X, X, O, X, O,
O, X, O, O, X, O, X, O, 
O, X, O, O, X, O, X, O, 
O, X, O, O, X, O, X, O, 
O, X, O, O, X, O, X, O
  ]
for i in range(0,10):
    sense.set_pixels(HELLO)
    time.sleep(1)
    sense.clear()
    time.sleep(1)
sense.show_message("IT WORKED! YOU DID IT!!")
