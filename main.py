
from machine import Pin, SPI
import gc9a01
import time
import random
from micropython import const
import vga2_8x16 as font

#import vga2_bold_16x32 as font
VSPI = const(2)
HSPI = const(1)


def main():
    spi = SPI(2, baudrate=60000000, sck=Pin(18), mosi=Pin(23))
    tft = gc9a01.GC9A01(
        spi,
        cs=Pin(5, Pin.OUT),
        dc=Pin(16, Pin.OUT),
        reset=Pin(17, Pin.OUT),
        backlight=Pin(22, Pin.OUT),
        rotation=0
        )
    tft.fill(0)
    
    color = gc9a01.color565(128, 255, 128)
    
    tft.line(1, 1, 239, 239, color)
    tft.line(1, 239, 239, 1, color)

    for i in range(5):
        tft.line(10, 120, 235, 60+(i*20), color)
    data = [40, 20, 30, 70]
    color = gc9a01.color565(50, 50, 255)
    for i in range(len(data)):
        #negative height does not work
        tft.fill_rect(100 + i * 15, 160-data[i], 10, data[i], color)
    
    tft.text(font, "agassi a kiraly", 50, 30, gc9a01.color565(255, 30, 30))
    
    for i in range(3):
        tft.circle((120-50) + i * 45, 210, 15, gc9a01.WHITE)
    
    print("Done")

main()