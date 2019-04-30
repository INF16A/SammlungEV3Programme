#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here

motor_l = Motor(Port.B)
motor_r = Motor(Port.C)
robot = DriveBase(motor_l, motor_r, 56, 114) # wheel diameter (mm) | axle track (mm)
color_sensor = ColorSensor(Port.S3)

# function helper:
# motor_l.run_target(degreesPerSecond, degrees)
# color_sensor.ambient() # ReturnsAmbient light intensity, ranging from 0 (dark) to 100 (bright).
# robot.drive(speed, steering) # mm/s | deg/s

max_speed = 40
max_steer = 20

global maximum, direction
direction = False
maximum = 0
def reverseDirection():
    global maximum, direction
    direction = not direction
    maximum = 0


while True:
    # read brightness value from color sensor
    brightness = color_sensor.ambient()
    # check if light source is reached (brightness goes to 50)
    if brightness < 50:
        
        if direction: # turning slightly right
            robot.drive(max_speed, max_steer)
        else: # turning slightly left
            robot.drive(max_speed, -max_steer)

        # when turning more towards light source, save that as new maximum
        if brightness >= maximum:
            global maximum
            maximum = brightness
        else: # when turning away from light source, reverse the sweeping direction
            reverseDirection()
    else: # if light source is reached, stop the motors
        robot.stop()
    wait(10)
