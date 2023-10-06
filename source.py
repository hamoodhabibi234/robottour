#imports libraries
import gpiozero
import time
import math
from time import sleep
from gpiozero import PhaseEnableRobot, Button
robot = PhaseEnableRobot(left=(11, 12), right=(15, 16))
tof1 = Button(35)
tof2 = Button(36)
tof3 = Button(37)
tof4 = Button(38)
tofa = Button(29)
tofb = Button(31)
tofc = Button(32)
tofd = Button(33)
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
    if(column1 == 1):
      while not(tof1.is_pressed & tofa.is_pressed):
        robot.left()
    elif(column1 == 2):
      while not(tof2.is_pressed & tofb.is_pressed):
        robot.left()
    elif(column1 == 3):
      while not(tof3.is_pressed & tofc.is_pressed):
        robot.left()
    elif(column1 == 4):
      while not(tof4.is_pressed & tofd.is_pressed):
        robot.left()
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
