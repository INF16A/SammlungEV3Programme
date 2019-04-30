#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Initialize Motors
motorLeft = Motor(Port.A)
motorRight = Motor(Port.B)
robot = DriveBase(motorLeft, motorRight, 56, 114)

# Initialize Color Sensor
colorSensor = ColorSensor(Port.S1)

# Set Base Color
baseColor = colorSensor.color()

while True: 
    robot.drive(200,0)

    while baseColor != colorSensor.color():
        robot.drive_time(0,45,1)
        

