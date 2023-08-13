import gpiozero
import time
from gpiozero import PhaseEnableRobot, Button

robot = PhaseEnableRobot(left=(11, 12), right=(15, 16))
hdg90 = Button(29)
hdg180 = Button(31)
hdg270 = Button(33)
hdg360 = Button(35)
tof1 = Button(36)
tof2 = Button(38)
tof3 = Button(40)
start = Button(13)

a = 1
b = 2
c = 3
d = 4

startpoint = input("enter starting coordinates:")
gz1 = input("enter closest gate zone coordinates:")
gz2 = input("enter middle gate zone coordinates:")
gz3 = input("enter furthest gate zone coordinates:")
endpoint = input("enter ending coordinates:")
target = input("target time here")

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

start.wait_for_press(timeout=None)
start = time.time()
end = time.time()

for i in range(1):
  #enter code below this

  while end - start < target:
    robot.right()
    time.sleep(0.1)
    end = time.time()
    robot.left()
    time.sleep(0.1)
    end = time.time()
  
