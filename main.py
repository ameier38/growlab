from time import sleep
from typing import Any
import RPi.GPIO as GPIO
import smbus

MAX_ADC_VALUE = 254

class ADS7830:
    def __init__(self):
        self.cmd = 0x84
        # check using command `i2cdetect -y 1` on your Pi
        # 0x4b is the default i2c address for ADS7830 Module.   
        self.address = 0x4b
        self.bus=smbus.SMBus(1)
        self._validate()
        
    def _validate(self):
        try:
            self.bus.write_byte(self.address,0)
            print("Successfully connected to ADS77830")
        except:
            raise ConnectionError(f"ADS77830 not found on address 0x{self.address}")

    def analog_read(self, chn): # ADS7830 has 8 ADC input pins, chn:0,1,2,3,4,5,6,7
        return self.bus.read_byte_data(self.address, self.cmd|(((chn<<2 | chn>>1)&0x07)<<4))
            
    def close(self):
        self.bus.close()

class Motor:
    motor_in_1_pin: int
    motor_in_2_pin: int
    enable_pin: int
    adc: ADS7830
    pwm: Any

    def __init__(self, motor_in_1_pin: int, motor_in_2_pin: int, enable_pin: int) -> None:
        self.motor_in_1_pin = motor_in_1_pin
        self.motor_in_2_pin = motor_in_2_pin
        self.enable_pin = enable_pin
        self.adc = ADS7830()
        self._setup_gpio()
        

    def _setup_gpio(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motor_in_1_pin, GPIO.OUT)
        GPIO.setup(self.motor_in_2_pin, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        self.pwm = GPIO.PWM(self.enable_pin, 1000)
        self.pwm.start(0)

    @staticmethod
    def _normalize_adc_value(value, from_low, from_high, to_low, to_high):
        return (value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low

    def _run(self, adc_value:int):
        print(f"adc_value: {adc_value}")
        GPIO.output(self.motor_in_1_pin, GPIO.HIGH)
        GPIO.output(self.motor_in_2_pin, GPIO.LOW)
        if adc_value > 50:
            GPIO.output(self.motor_in_1_pin, GPIO.LOW)
            GPIO.output(self.motor_in_2_pin, GPIO.HIGH)
        else:
            GPIO.output(self.motor_in_1_pin, GPIO.LOW)
            GPIO.output(self.motor_in_2_pin, GPIO.LOW)
        normalized_adc_value = self._normalize_adc_value(adc_value, 0, MAX_ADC_VALUE, 0, 100)
        print(f"normalized_adc_value: {normalized_adc_value}")
        self.pwm.start(normalized_adc_value)

    def start(self):
        while True:
            adc_value = self.adc.analog_read(0)
            sleep(0.1)
            self._run(adc_value)

def run():
    motor = Motor(motor_in_1_pin=13, motor_in_2_pin=11, enable_pin=15)
    motor.start()

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print("Program starting...")
    try:
        run()
    except KeyboardInterrupt:
        destroy()
