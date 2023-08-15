#imports libraries
import gpiozero
import time
import smbus
import math
from time import sleep
from gpiozero import PhaseEnableRobot, Button
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
#defines pins
robot = PhaseEnableRobot(left=(11, 12), right=(15, 16))
hdg90 = Button(29)
hdg180 = Button(31)
hdg270 = Button(33)
hdg360 = Button(35)
tof1 = Button(36)
tof2 = Button(38)
tof3 = Button(40)
start = Button(13)
#sets letter variables
a = 1
b = 2
c = 3
d = 4
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
#actual code
for i in range(1):
  #enter code below this

  #end wait code
  while end - start < target:
    robot.right()
    time.sleep(0.1)
    end = time.time()
    robot.left()
    time.sleep(0.1)
    end = time.time()
  
