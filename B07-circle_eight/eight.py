#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

motorL = Motor(Port.B)
motorR = Motor(Port.C)
brick.display.text("Run eight", (60, 50))
robot = DriveBase(motorL, motorR, 56, 104) # wheel diameter (mm) | axle track (mm) !!!!!!!!!!!! ACHSENABSTAND MUSS ANGEPASST WERDEN

while True:
    robot.drive_time(300, 44, 8181) # mm/s | deg/s circle right 9 secs
    robot.drive_time(300, -44, 8181) # circle left 9 secs