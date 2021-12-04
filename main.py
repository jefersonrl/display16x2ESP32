from time import sleep_ms, ticks_ms 
from machine import I2C, Pin 
from i2c_lcd import I2cLcd 

DEFAULT_I2C_ADDR = 0x27

i2c = I2C(scl=Pin(22), sda=Pin(21), freq=400000) 
lcd = I2cLcd(i2c, DEFAULT_I2C_ADDR, 2, 16)
count = 0

while True:
    lcd.putstr('Counter: {}' .format(count))
    count = count + 1
    sleep_ms(1000)
    lcd.clear()