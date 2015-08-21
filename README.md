# PiPaint
Pi project for Pi class

The user will be able to touch pad and draw on the LED display. They will be able to choose the size of the pen or brush and erase the display by pressing buttons. Since it’s a resistive touch pad the user will be able to use either their finger or a stylus to draw.

The target audience of this project are people who like to draw or doodle, people who like pixel art and kids.

###Materials:
- Raspberry Pi
- Arduino Uno
- 16x32 RGB LED Matrix
- Female to female jumpers
- 5v 2A power supply
- Female D/C power adapter
- Resistive Touchscreen Overlay (7" diag. 165mm x 105mm - 4 wire)
- STMPE610 Resistive Touch Screen Controller
- A few buttons (~3)
- Some male to male wires and jumpers


I got all of the materials from [Adafruit](https://www.adafruit.com/)

##Prior Art

LED touchpad Sketch
I didn't know about this before starting proposing my project but a group of Cornell University students did a project like this where you can touch a touch pad and have the LEDs in a matrix light up depending on the touch input. They used a microcontroller instead of the Pi and Arduino and a different LED Matrix. The details of their project can be found [here at Cornell's site](http://people.ece.cornell.edu/land/courses/ece4760/FinalProjects/f2014/qw77_yq83_zm84/qw77_yq83_zm84/index.html).


###Libraries
+ Adafruit’s [STMPE610 library](https://github.com/adafruit/Adafruit_STMPE610)
+ Hzeller’s [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix/)

###Tutorials
+ [Adafruit’s Connecting a 16x32 RGB LED Matrix Panel to a R  aspberry Pi](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi?view=all)

##License
GNU General Public License v2.0

####Hzeller rpi-rgb-led-Matrix
I didn't change anything the library. I just added more classes of my own.

