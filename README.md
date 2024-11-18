# esp32-gc9a01-tft
Circular TFT screen is controlled by ESP32 and gc9a01 driver written in micropython
based on Russ Hughes's repository
https://github.com/russhughes/gc9a01_mpy and https://github.com/russhughes/gc9a01py

ESP 32 Firmware
https://micropython.org/download/ESP32_GENERIC/




# Methods
[GC9A01](#GC9A01) <br>
[hard_reset](#hard_reset) <br>
[soft_reset](#soft_reset) <br>
[sleep_mode](#sleep_mode) <br>
[inversion_mode](#inversion_mode) <br>
[rotation](#rotation) <br>
[vline](#vline) <br>
[hline](#hline) <br>
[pixel](#pixel) <br>
[rect](#rect) <br>
[circle](#circle) <br>
[fill_rect](#fill_rect) <br>
[fill_circle](#fill_circle) <br>
[text](#text) <br>
[vscsad](#vscsad) <br>
[vscrdef](#vscrdef) <br>

## GC9A01 constructor

## hard_reset
Resets TFT via wires

## soft_reset
Resets TFT via reset command

## sleep_mode
Enable or disable display sleep mode.

**Args:**

    value (bool): 
        if True enable sleep mode.
        if False disable sleep mode

## inversion_mode
Enable or disable display inversion mode.

**Args:**

    value (bool): if True enable inversion mode.
        if False disable inversion mode

## rotation
Sets the orientation of the TFT

    ROTATIONS = [
        0 - PORTRAIT
        1 - LANDSCAPE
        2 - INVERTED_PORTRAIT
        3 - INVERTED_LANDSCAPE
        4 - PORTRAIT_MIRRORED
        5 - LANDSCAPE_MIRRORED
        6 - INVERTED_PORTRAIT_MIRRORED
        7 - INVERTED_LANDSCAPE_MIRRORED
    ] 

## vline
Draws vertical line at the given location and color <code>color</code>

**Args:**

    x (int): x coordinate
    Y (int): y coordinate
    length (int): length of line
    color (int): 565 encoded color

## hline
Draws horizontal line at the given location and color <code>color</code>

**Args:**

    x (int): x coordinate
    Y (int): y coordinate
    length (int): length of line
    color (int): 565 encoded color

## line
Draws line with specified color in any direction 

## pixel
Sets a pixel to at specified location <code>x0, y0</code> to specified color <code>color</code>

## rect
Draws a rectangle border at set location <code>x, y</code>  with specified width <code>w</code>, height <code>h</code>, and color <code>color</code>

## circle
Draws circle at specified center <code>x0, y0</code> with specified radius <code>r</code> and color <code>color</code>

## fill_rect
Same as [`rect`](#rect), and fills the rectangle with color <code>color</code>

## fill_circle
Same as [`circle`](#circle), and fills the rectangle with color <code>color</code>

## text
Draw text on display in specified font and colors. 8 and 16 bit wide fonts are supported. Font .py must be available in ESP.

## vscrdef
Set Vertical Scrolling Definition.

To scroll a 135x240 display these values should be 40, 240, 40. There are 40 lines above the display that are not shown followed by 240 lines that are shown followed by 40 more lines that are not shown. You could write to these areas off display and scroll them into view by changing the TFA, VSA and BFA values.

**Args:**

      tfa (int): Top Fixed Area
      vsa (int): Vertical Scrolling Area
      bfa (int): Bottom Fixed Area

## vscsad

Set Vertical Scroll Start Address of RAM.

Defines which line in the Frame Memory will be written as the first line after the last line of the Top Fixed Area on the display

## write (untested)
Write a string using a converted true-type font on the display starting at the specified column and row

## bitmap (untested)
Draw a bitmap on display at the specified column and row

## Color constants
    BLACK = const(0x0000)
    BLUE = const(0x001F)
    RED = const(0xF800)
    GREEN = const(0x07E0)
    CYAN = const(0x07FF)
    MAGENTA = const(0xF81F)
    YELLOW = const(0xFFE0)
    WHITE = const(0xFFFF)