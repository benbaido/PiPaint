#=================================
#   imports
#=================================
import RPi.GPIO as GPIO
import time 

import serial       #for reading serial input from arduino
import string

#=================================
#   GPIO set up
#=================================
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

reset_btn = 5
erase_toggle_btn = 6
color_set_btn = 13

#=================================
#   pin config for matrix
#=================================
#for top half of matrix
red1_pin = 17
green1_pin = 27
blue1_pin = 22

#for bottom half of matrix
red2_pin = 23
green2_pin = 24
blue2_pin = 25

a_pin = 7
b_pin = 8
c_pin = 9

clock_pin = 3
latch_pin = 4
oe_pin = 2

#=================================
#   variables
#=================================
delay = 0.000001

#panit mode: 1 = brush mode; 0 = erase mode
paint_mode = 1

#brush color
last_color = 0
brush_color = 2

#for comparing points from touch screen
temp_point = ['0', '0', '0']

screen = [[0 for x in xrange(32)] for x in xrange(16)]

#=================================
#   set up serial input
#=================================
arduino_data = serial.Serial('/dev/ttyACM0', 9600)
#arduino_data.open()
#arduino_data.write("testing...")

#=================================
#   set pins to output
#=================================
GPIO.setup(red1_pin, GPIO.OUT)
GPIO.setup(blue1_pin, GPIO.OUT)
GPIO.setup(green1_pin, GPIO.OUT)

GPIO.setup(red2_pin, GPIO.OUT)
GPIO.setup(blue2_pin, GPIO.OUT)
GPIO.setup(green2_pin, GPIO.OUT)

GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)

GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)

#=================================
#   set buttons to input
#=================================
GPIO.setup(reset_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(erase_toggle_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(color_set_btn, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#=================================
#   matrix set up control functions
#       from adafruit
#       http://github.com/hzeller/rpi/rpi-rgb-led-matrix
#       http://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi
#
#=================================

def clock():
    GPIO.output(clock_pin, 1)
    GPIO.output(clock_pin, 0)

def latch():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)

def bits_from_int(x):
    a_bit = x & 1
    b_bit = x & 2
    c_bit = x & 4
    return (a_bit, b_bit, c_bit)

def set_row(row):
    #time.sleep(delay)
    a_bit, b_bit, c_bit = bits_from_int(row)
    GPIO.output(a_pin, a_bit)
    GPIO.output(b_pin, b_bit)
    GPIO.output(c_pin, c_bit)
    #time.sleep(delay)

def set_color_top(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red1_pin, red)
    GPIO.output(green1_pin, green)
    GPIO.output(blue1_pin, blue)
    #time.sleep(delay)

def set_color_bottom(color):
    #time.sleep(delay)
    red, green, blue = bits_from_int(color)
    GPIO.output(red2_pin, red)
    GPIO.output(green2_pin, green)
    GPIO.output(blue2_pin, blue)
    #time.sleep(delay)

def refresh():
    for row in range(8):
        GPIO.output(oe_pin, 1)
        set_color_top(0)
        set_row(row)
        #set_color_bottom(0)
        #time.sleep(delay)
        for col in range(32):
            #print "row: " + str(row) + " col: " + str(col)
            set_color_top(screen[row][col])
            set_color_bottom(screen[row+8][col])
            clock()

        latch()
        GPIO.output(oe_pin, 0)
        time.sleep(delay)

def fill_rectangle(x1, y1, x2, y2, color):
    for x in range(x1, x2):
        for y in range(y1, y2):
            screen[y][x] = color

def set_pixel(x, y, color):
    screen[x][y] = color

#=================================
#   my functions
#=================================
#   LED Matrix
#---------------------------------
####################################
#the turn off/on doesn't really work
def turn_on_leds_in_matrix():
    for x in range(16):
        for y in range(32):
            set_pixel(x, y, 7)
    refresh()

def turn_off_leds_in_matrix():
    for x in range(16):
        for y in range(32):
            set_pixel(x, y, 0)
    refresh()
######################################
def blinkLED(x, y, color):
    set_pixel(x, y, color)
    refresh()
    set_pixel(x, y, 0)

def rainbow_intro_slider():
    color = 1

    for x in range(16):

        if(color == 7):
            color = 1
        else:
            color = color + 1

        #print "color: " +str(color)
        #print "x: " + str(x)
        
        for y in range(32):
            #print " y: " + str(y)
            set_pixel(x, y, color)
            refresh()
            #print "x: " + str(x) + " y: " + str(y)
            #time.sleep(0.25)
            #set_pixel(x, y, 0)
            #refresh()
            
    #turn off
    for x in reversed(xrange(16)):
        for y in reversed(xrange(32)):
            set_pixel(x, y, 0)
            refresh()

def rainbow_slider(color=3):
    for x in range(16):
        #print "color: " +str(color)
        #print "x: " + str(x)
        
        for y in range(32):
            #print " y: " + str(y)
            set_pixel(x, y, color)
            refresh()
            
    #turn off
    for x in reversed(xrange(16)):
        for y in reversed(xrange(32)):
            set_pixel(x, y, 0)
            refresh()

def is_new_point(old_point, new_point):
    if(old_point[0] == new_point[0] and old_point[1] == new_point[1]):
        return False
    return True
    
def is_pressure_zero(point):
    if(point[2] == 0):
        return True
    return False

#---------------------------------
#   Buttons
#---------------------------------
def resetMatrix(channel):
    if(GPIO.input(reset_btn)):
        global brush_color
        print "reseting..."
        #if the reset button is pressed
        #run rainbow slider once to clear board
        rainbow_slider(brush_color)

def changeBrushColor(channel):
    global brush_color
    global paint_mode
    if(paint_mode == 1):
        if(brush_color >= 7):
            brush_color = 1
        else:
            brush_color = brush_color + 1
            
        print "brush color changed! color now: " + str(brush_color)
    else:
        print "currently in erase mode"
    

def changePaintMode(channel):
    global paint_mode
    global brush_color
    global last_color
    
    if(paint_mode == 1):
        #change to erase mode
        paint_mode = 0
        #save last used color
        last_color = brush_color
        #change brush color
        brush_color = 0
        print "Now in Erase Mode!"
    else:
        #change to paint mode
        paint_mode = 1
        brush_color = last_color
        print "Now in draw mode!"

#=================================
#   interrupts
#=================================
GPIO.add_event_detect(reset_btn, GPIO.RISING, callback=resetMatrix)
GPIO.add_event_detect(erase_toggle_btn, GPIO.RISING, callback=changePaintMode)
GPIO.add_event_detect(color_set_btn, GPIO.RISING, callback=changeBrushColor)

#--------------------------------
# should I make this an interrupt too? how?
#--------------------------------
while True:
    #rainbow_intro_slider()
    #refresh()
    
    try:
        #blinkLED(15, 31, 3)
        #refresh()
        while (arduino_data.inWaiting() == 0 ):
             #if there is no data input don't do anything
            pass

        coordinates = arduino_data.readline()   #get the line from serial port
        coordinates = coordinates.rstrip("\r\n")
        point = coordinates.split(",")          #split input into x, y, z

        if(not is_new_point(temp_point, point)):
            #print "same point"
            pass
        else:
            print "temp: ", temp_point
            print "point: ", point
            print "different point"
            print "---------------"
            temp_point[0] = point[0]
            temp_point[1] = point[1]
            temp_point[2] = point[2]
            point_x = int(point[0])                 #get x coordinate
            point_y = int(point[1])                 #get y coordiante
            point_z = int(point[2])                 #get pressure
            set_pixel(point_y, point_x, brush_color)
            #refresh()

        refresh()
        
    except Exception as e:
        print e
        
    refresh()
    
arduino_data.close()
GPIO.cleanup()
