from machine import Pin, SPI#, SoftI2C
import gc9a01
import time
import random
from micropython import const
import vga2_8x16 as font

BOARD_I2C_SCL_PORT = const(5)
BOARD_I2C_SDA_PORT = const(4)

# import vga2_bold_16x32 as font
VSPI = const(2)
HSPI = const(1)

CS_PIN = const(5)
DC_PIN = const(16)
RESET_PIN = const(4)
BACKLIGHT_PIN = const(0)


class MockDataProvider:
    def __init__(self):
        pass

    def hasData(self):
        return True

    def getData(self):
        return random.randint(0, 60)


def board_configuration():
    spi = SPI(VSPI, baudrate=60000000, sck=Pin(18), mosi=Pin(23))
    tft = gc9a01.GC9A01(
        spi,
        cs=Pin(CS_PIN, Pin.OUT),
        dc=Pin(DC_PIN, Pin.OUT),
        reset=Pin(RESET_PIN, Pin.OUT),
        backlight=Pin(BACKLIGHT_PIN, Pin.OUT),
        rotation=0,
    )
    # i2c = SoftI2C(scl=Pin(BOARD_I2C_SCL_PORT), sda=Pin(BOARD_I2C_SDA_PORT))
    # print(i2c.scan())
    tft.fill(0)
    return tft


def main():

    tft = board_configuration()
    dataProv = MockDataProvider()
    # history
    history = []
    history_max = 60
    bar_width = 3
    bar_width_plus_gap = 4
    index = -1
    active_color = gc9a01.color565(100, 100, 220)
    inactive_color = gc9a01.color565(30, 30, 200)
    bg_color = gc9a01.color565(0, 0, 0)

    while dataProv.hasData():
        # Mock data provider
        datum = dataProv.getData()

        # remove existing bar
        if len(history) == history_max:
            history_value = history[index]
            tft.fill_rect(
                0 + index * bar_width_plus_gap,
                120 - 30,
                width=bar_width,
                height=60,
                color=bg_color,
            )
             
        # store datum in history
        if len(history) < history_max:
            history.append(datum)
        else:
            
            history[index] = datum
        
        #redraw value in history
        tft.fill_rect(
                0 + (index) * bar_width_plus_gap,
                120 - history[index] // 2,
                width=bar_width,
                height=history[index],
                color=inactive_color,
            )
        

        index = (index + 1) % history_max
        
        
        
        # draw new bar
        tft.fill_rect(
            0 + index * bar_width_plus_gap,
            120 - datum // 2,
            width=bar_width,
            height=datum,
            color=active_color,
        )
        
        
        text = " data: " + str(datum) + " "
        tft.text(font, text, 120 - len(text) * 8 // 2, 40, gc9a01.WHITE, gc9a01.BLACK)

        time.sleep(0.2)
        # for i in range(len(data)):
        # negative height does not work


main()
