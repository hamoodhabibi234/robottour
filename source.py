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

start.wait_for_press(timeout=None)
start = time.time()
end = time.time()
target = 1 #target time here

for i in range(1):
  #enter code below this

  while end - start < target:
    robot.right()
    time.sleep(0.1)
    end = time.time()
    robot.left()
    time.sleep(0.1)
    end = time.time()
  
