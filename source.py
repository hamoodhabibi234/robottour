#imports libraries
import gpiozero
import time
import math
import smbus
from time import sleep
from gpiozero import PhaseEnableRobot, Button, AngularServo
#mpu stuff
#some MPU6050 Registers and their Address
Register_A     = 0              #Address of Configuration register A
Register_B     = 0x01           #Address of configuration register B
Register_mode  = 0x02           #Address of mode register
X_axis_H    = 0x03              #Address of X-axis MSB data register
Z_axis_H    = 0x05              #Address of Z-axis MSB data register
Y_axis_H    = 0x07              #Address of Y-axis MSB data register
declination = 0.7505         #define declination angle of location where measurement going to be done
pi          = 3.14159265359     #define pi value
def Magnetometer_Init():
        #write to Configuration Register A
        bus.write_byte_data(Device_Address, Register_A, 0x70)

        #Write to Configuration Register B for gain
        bus.write_byte_data(Device_Address, Register_B, 0xa0)

        #Write to mode Register for selecting mode
        bus.write_byte_data(Device_Address, Register_mode, 0)
	
def read_raw_data(addr):
    
        #Read raw 16-bit value
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from module
        if(value > 32768):
            value = value - 65536
        return value

bus = smbus.SMBus(1) 	# or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x1e   # HMC5883L magnetometer device address
Magnetometer_Init()     # initialize HMC5883L magnetometer 
#sets pins
robot = PhaseEnableRobot(left=(11, 12), right=(15, 16))
tof1 = Button(35)
tof2 = Button(36)
tof3 = Button(37)
tof4 = Button(38)
servo = AngularServo(40, min_angle=-90, max_angle=90)
start = Button(13)
#sets letter variables
a = 4
b = 3
c = 2
d = 1
#asks input
startpoint = input("enter starting coordinates:")
gz1 = input("enter closest gate zone coordinates:")
gz2 = input("enter middle gate zone coordinates:")
gz3 = input("enter furthest gate zone coordinates:")
endpoint = input("enter ending coordinates:")
target = input("target time here")
#defines compass
def bearing(): #Read Accelerometer raw value
        x = read_raw_data(X_axis_H)
        z = read_raw_data(Z_axis_H)
        y = read_raw_data(Y_axis_H)

        heading = math.atan2(y, x) + declination
        
        #Due to declination check for >360 degree
        if(heading > 2*pi):
                heading = heading - 2*pi

        #check for sign
        if(heading < 0):
                heading = heading + 2*pi

        #convert into angle
        heading_angle = int(heading * 180/pi)
#sets variables
heading_angle = 0
row1 = startpoint[1]
row2 = gz1[1]
row3 = gz2[1]
row4 = gz3[1]
row5 = endpoint[1]
column1 = startpoint[0]
column2 = gz1[0]
column3 = gz2[0]
column4 = gz3[0]
column5 = endpoint[0]
#waits for start
start.wait_for_press(timeout=None)
start = time.time()
end = time.time()
#actual code
for i in range(1):
  #enter code below this
#code that makes the robot go to start location
  while not(tof4.is_pressed):
    robot.forward()
  robot.stop()
  if(row2 == 1):
    while not(tof1.is_pressed):
      robot.forward()
    robot.stop()
  elif(row2 == 2):
    while not(tof2.is_pressed):
      robot.forward()
    robot.stop()
  elif(row2 == 3):
    while not(tof3.is_pressed):
      robot.forward()
    robot.stop()
  elif(row2 == 4):
    robot.stop()
  if(column1 > column2):
    while not(heading_angle == heading_angle + 90):
      robot.right()
      bearing()
    robot.stop()
  elif(column1 < column2):
    while not(heading_angle == heading_angle - 90):
      robot.left()
      bearing()
    robot.stop()
  elif(column1 == column2):
    robot.stop()
  #end wait code
  while(end - start < target - 10):
    robot.right()
    time.sleep(0.1)
    end = time.time()
    robot.left()
    time.sleep(0.1)
    end = time.time()
  robot.stop()
