import gpiozero
import time
from gpiozero import PhaseEnableRobot, Button

robot = PhaseEnableRobot(left=(11, 12), right=(15, 16))
hdg90 = Button(13)
hdg180 = Button(13)
hdg270 = Button(13)
hdg360 = Button(13)
tof1 = Button(18)
tof2 = Button(18)
tof3 = Button(18)
start = Button(22)

start.wait_for_press(timeout=None)
start = time.time()
end = time.time()
target = 1 #target time here

for i in range(1):
  robot.forward()
  #enter code below this

  while {end-start}<target:
    robot.right()
    time.sleep(0.1)
    end = time.time()
    robot.left()
    time.sleep(0.1)
    end = time.time()
  
