# PiPaint
Pi project for Pi class

Users the draw on the LED Matrix using the touchscreen overlay.
Users are able to draw change the color of the LEDs that light up, reset the screen and 

The target audience of this project are people who like to draw or doodle, people who like pixel art and kids.

###Materials:
- [Raspberry Pi 2](https://www.adafruit.com/products/2358)
- [Arduino Uno](https://www.adafruit.com/products/50)
- [16x32 RGB LED Matrix](https://www.adafruit.com/product/420)
- Female to female jumpers
- 5v 2A power supply
- Female D/C power adapter
- [Resistive Touchscreen Overlay (7" diag. 165mm x 105mm - 4 wire)](https://www.adafruit.com/products/1676)
- [STMPE610 Resistive Touch Screen Controller](https://www.adafruit.com/products/1571)
- A few buttons (~3)
- Some male to male wires and jumpers


I got all of the materials from [Adafruit](https://www.adafruit.com/)

####LED Matrix
The RGB LED Matrixs don't have datasheets attached to them.

They also don't have a built in PWM control. You have to manually redraw over the matrix.

More information on the board can be found [here](https://learn.adafruit.com/32x16-32x32-rgb-led-matrix?view=all) along with the pin maps for the input and output pins.

###Resistive Touchscreen Overlay
This touch screen is made of glass so be careful with it. It only has touch on one side. Mine had touch with the black part of the strip facing up. Where the strip is is the bottom of the overlay. You can use a stylus with this overlay.

####STMPE610
+ [datasheet](http://www.adafruit.com/datasheets/STMPE610.pdf)

The datasheet Adafruit provides for the board it outdated and doesn't have the right pin layout but the information is correct. The y+, y-, x+ and x- pins are at the top of the board while the other pins are lined up at the bottom of the board. 

To connect it to the arduino, just follow the instructions in the library's example code.

##Files
###pipaint_two.py
This is the program to run on the pi. It sets up the LED Matrix, sets up serial communication to the Arduino so the Pi can get the touch data. 

###testarduino.py
This is to test the serial connection beteen the pi and the Arduino. It's not part of the program.

###TouchTest_adaex.ino
This is the file to uplaod into the arduino. It gets the touch data from the touchscreen overlay and inputs the data to the serial screen as x, y, and z, seperated by a comma.

For the pi to read the serial input correctly the serial monitor has to be closed on the Arduino side. If the serial monitor is up some inputs won't be transfered and some won't. The data transfered won't be complete.

##Issues
LED Matrix

For some reason only row of LEDs will continuously light up and at the right brightness. The other LEDs are dim and will only light up when there's currently touch input streaming in. Could use threading to try to solve this problem.

While presenting the project colors other than red and a very dim green wouldn't show up even though they did during testing (maybe I just put the matrix pin to the wrong pins on the pi)

##Prior Art

*LED touchpad Sketch*

I didn't know about this before starting proposing my project but a group of Cornell University students did a project like this where you can touch a touch pad and have the LEDs in a matrix light up depending on the touch input. They used a microcontroller instead of the Pi and Arduino and a different LED Matrix. The details of their project can be found [here at Cornell's site](http://people.ece.cornell.edu/land/courses/ece4760/FinalProjects/f2014/qw77_yq83_zm84/qw77_yq83_zm84/index.html).

###Libraries
+ Adafruit’s [STMPE610 library](https://github.com/adafruit/Adafruit_STMPE610)
+ Hzeller’s [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix/)
+ pyserial

###Tutorials
+ [Adafruit’s Connecting a 16x32 RGB LED Matrix Panel to a R  aspberry Pi](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi?view=all)

##License
GNU General Public License v2.0
[http://www.gnu.org/licenses/gpl-2.0.txt]](http://www.gnu.org/licenses/gpl-2.0.txt)

####Hzeller rpi-rgb-led-Matrix
This library is under the GNU General Public License v2.0.

I didn't change anything the library. I just added more classes of my own.

####Adafruit's STMPE610
This library is under the MIT license.

