MAX_ADC_VALUE = 254

import smbus

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
