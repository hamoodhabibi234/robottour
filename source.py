#imports libraries
import gpiozero
import time
import smbus
import math
from time import sleep
from gpiozero import PhaseEnableRobot, Button, Servo
#registers mpu
Register_A     = 0
Register_B     = 0x01
Register_mode  = 0x02 

X_axis_H    = 0x03
Z_axis_H    = 0x05
Y_axis_H    = 0x07
declination = -0.06487
pi = 3.14159265359   

def Magnetometer_Init():
        #write to Configuration Register A
        bus.write_byte_data(Device_Address, Register_A, 
        0x70)

        #Write to Configuration Register B for gain
        bus.write_byte_data(Device_Address, Register_B, 
        0xa0)

        #Write to mode Register for selecting mode
        bus.write_byte_data(Device_Address, Register_mode, 
        0)
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
#defines pins
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
#sets variables
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
hdg = 0
        #Read Accelerometer raw value
        x = read_raw_data(X_axis_H)
        z = read_raw_data(Z_axis_H)
        y = read_raw_data(Y_axis_H)
        hdg = math.atan2(y / x) + declination
        #Due to declination check for >360 degree
        if(hdg > 2*pi)
                hdg = hdg - 2*pi
        #check for sign
        if(hdg < 0):
                hdg = hdg + 2*pi
        #convert into angle
        hdg_angle = int(hdg * 180/pi)

#actual code
for i in range(1):
  #enter code below this
#code that makes the robot go to start location
  while not(tof1.is_pressed):
    robot.forward
  robot.stop
  #does math for first checkpoint
  ang1rad = math.atan((row1-row2)/(column1-column2))
  ang1 = math.degrees(ang1rad)
  if(abs(ang1) != ang1):
    ang1 = ang1 + 360
  if(abs(row1-row2) != row1-row2):
    ang1 = ang1 + 180
  if(ang1 >= 360):
    ang1 = ang1 - 360
  #movement code for 1st checkpoint below
  inithdg = hdg_angle + 360
  posthdg = hdg_angle + 360
  deviation = posthdg - inithdg
  while not(deviation == ang1):{
    robot.right()
        #Read Accelerometer raw value
        x = read_raw_data(X_axis_H)
        z = read_raw_data(Z_axis_H)
        y = read_raw_data(Y_axis_H)
        hdg = math.atan2(y / x) + declination
        #Due to declination check for >360 degree
        if(hdg > 2*pi)
                hdg = hdg - 2*pi
        #check for sign
        if(hdg < 0):
                hdg = hdg + 2*pi
        #convert into angle
        hdg_angle = int(hdg * 180/pi)
        posthdg = hdg_angle + 360
        deviation = posthdg - inithdg
  }
  robot.stop
  if(deviation <= 180 and deviation >= 91):
    servo.angle = 180 - deviation
    
    
  #end wait code
  while end - start < target:
    robot.right()
    time.sleep(0.1)
    end = time.time()
    robot.left()
    time.sleep(0.1)
    end = time.time()
  robot.stop
