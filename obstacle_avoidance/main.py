#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

obstacle_sensor = UltrasonicSensor(Port.S3)
gyro_sensor_front = GyroSensor(Port.S4)
# gyro_sensor_side = GyroSensor(Port.S2)
right_motor = Motor(Port.C)
left_motor = Motor(Port.B)
wheel_diameter = 56
axle_track = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

rotateAngle = 90

def start():
    while True:
        robot.drive(200, 0)
        while obstacle_sensor.distance() < 250:
            robot.stop()
            obstacle_avoidance()

def obstacle_avoidance(step = 2000, speed = 200, min_dist = 250):
    print('avoid')
    distance = 0

    rotate(rotateAngle)
    distance += drive_past(step, speed, min_dist)
    print('bottom finished')

    drive_past(step, speed, min_dist)
    print('right finished')

    robot.drive_time(speed, 0, distance)
    rotate(rotateAngle)
    print('top finished')

def drive_past(step, speed, min_dist):
    past_object = False
    distance = 0

    while not past_object:
        distance = distance + step
        robot.drive_time(speed, 0, step)
        rotate(-rotateAngle)
        past_object = obstacle_sensor.distance() > min_dist
        if not past_object:
            rotate(rotateAngle)

    return distance

def rotate(angle):
    if angle > 0:
        angle -= 10

    sign = 1 if angle >= 0 else -1
    gyro_sensor_front.reset_angle(0)
    while sign * gyro_sensor_front.angle() <= sign * angle:
        print(gyro_sensor_front.angle())
        gyro_angle = gyro_sensor_front.angle()
        if (gyro_angle * sign > 50): # hier fehlen die signs
            robot.drive_time(0, 50 * sign, 70)
        else:
            robot.drive_time(0, 150 * sign, 70)

start()