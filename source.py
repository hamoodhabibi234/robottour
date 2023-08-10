import gpiozero
import time
from gpiozero import PhaseEnableRobot

robot = PhaseEnableRobot(left=(17, 18), right=(27, 22))

for i in range(1):
  robot.forward()
