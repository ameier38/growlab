from time import sleep
from typing import Any
import RPi.GPIO as GPIO

def run():
    gpio_pin = 11
    # Use pin numbering (e.g., GPIO17 = pin 11)
    # NB: https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
    GPIO.setmode(GPIO.BOARD)
    # NB: setup pins as output
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)
    # NB: set pin 1 to 3.3V and pin 2 to 0V
    print("turning on")
    GPIO.output(gpio_pin, GPIO.HIGH)
    sleep(3)
    # NB: set both pins to 0V
    print("turning off")
    GPIO.output(gpio_pin, GPIO.LOW)

def cleanup():
    GPIO.cleanup()

if __name__ == '__main__':
    print("Program starting...")
    try:
        run()
    except KeyboardInterrupt:
        cleanup()
    finally:
        cleanup()
