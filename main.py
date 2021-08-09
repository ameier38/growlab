from time import sleep
from typing import Any
import RPi.GPIO as GPIO

class Switch:
    gpio_pin_1: int
    gpio_pin_2: int

    def __init__(self, gpio_pin_1: int, gpio_pin_2: int) -> None:
        self.gpio_pin_1 = gpio_pin_1
        self.gpio_pin_2 = gpio_pin_2
        self._setup_gpio()
        

    def _setup_gpio(self):
        # Use pin numbering (e.g., GPIO17 = pin 11)
        # NB: https://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering
        GPIO.setmode(GPIO.BOARD)
        # NB: setup pins as output
        GPIO.setup(self.gpio_pin_1, GPIO.OUT)
        GPIO.setup(self.gpio_pin_2, GPIO.OUT)

    def start(self, max_iterations: int):
        iteration = 0
        while iteration < max_iterations:
            # NB: set pin 1 to 3.3V and pin 2 to 0V
            GPIO.output(self.gpio_pin_1, GPIO.HIGH)
            GPIO.output(self.gpio_pin_2, GPIO.LOW)
            sleep(2)
            # NB: set both pins to 0V
            GPIO.output(self.gpio_pin_1, GPIO.LOW)
            GPIO.output(self.gpio_pin_2, GPIO.LOW)
            iteration += 1

def run():
    switch = Switch(gpio_pin_1=13, gpio_pin_2=11)
    switch.start(max_iterations=5)

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
