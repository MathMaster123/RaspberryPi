sense = SenseHat()

for i in reversed(range(0,10)):
    back_1=randint(0, 255)
    back_2=randint(0, 255)
    back_3=randint(0, 255)
    colour_1=randint(0, 255)
    colour_2=randint(0, 255)
    colour_3=randint(0, 255)
    c=(colour_1, colour_2, colour_3)
    b=(back_1, back_2, back_3)
    sense.show_letter(str(i))
    time.sleep(.5)
sense.show_message("Happy New Year!!!", text_colour=c, back_colour=b)
