import serial
import string

#arduino_usb = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
arduino_usb = serial.Serial('/dev/ttyACM0', 9600)
arduino_usb.open()
arduino_usb.write("testing...")

try:
    while 1:
        line = arduino_usb.readline()
        print "line: ", line

        line = line.rstrip("\r\n")
        point = line.split(",")

        #point_x = int(point[0])
        #point_y = int(point[1])
        #point_z = int(point[2])

        #point_x = point[0]
        #point_y = point[1]
        #point_z = point[2]

        #print "x: " + str(point_x)
        #print "y: " + str(point_y)
        #print "z: " + str(point_z)
        print "point: ", point
        
except Exception as e:
    print e
finally:
    arduino_usb.close()
