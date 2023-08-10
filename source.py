import gpiozero
import time
from gpiozero import PhaseEnableRobot, Button

robot = PhaseEnableRobot(left=(11, 12), right=(15, 16))
lspd = Button(26)
rspd = Button(16)
hdg = Button(21)
tof = Button(20)
start = Button(26)

for i in range(1):
  robot.forward()
