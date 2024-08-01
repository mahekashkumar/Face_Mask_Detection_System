from pyfirmata import Arduino, SERVO

port = 'COM3'

pin = 10

board = Arduino(port)

board.digital[pin].mode = SERVO


def rotateServo(pin, angle):
    board.digital[pin].write(angle)


def doorAutomate(val):
    if val == 0:
        rotateServo(pin, 170)
    elif val == 1:
        rotateServo(pin, 90)
