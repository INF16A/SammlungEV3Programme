#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import random

# Write your program here
# brick.sound.beep()

# colors:
# 1: black
# 2: blue
# 3: green
# 4: yellow
# 5: red
# 6: white
# 7: brown

motor_arm = Motor(Port.A)
motor_grabber = Motor(Port.D)
motor_l = Motor(Port.B)
motor_r = Motor(Port.C)
robot = DriveBase(motor_l, motor_r, 56, 114) # wheel diameter (mm) | axle track (mm)
ultrasonic = UltrasonicSensor(Port.S1)
color_sensor_ramp = ColorSensor(Port.S2)
collision_button = TouchSensor(Port.S3)
color_sensor_floor = ColorSensor(Port.S4)
watch = StopWatch()
# ultrasonic2 = UltrasonicSensor(Port.S3)

collision_threshhold = 200  # mm
maximum_ball_count = 20      # size of storage container
random_direction_change_interval = 5000
drive_speed = 200           # mm/s
rotation_speed = 90         # deg/s
calibration_surface = -1
calibration_ramp = -1

ball_count = 0

def collision_avoidance():
    dist = ultrasonic.distance()
    touch = collision_button.pressed()
    if touch:
            robot.drive_time(-drive_speed, 0, 500)
    if dist < collision_threshhold or touch:
        robot.drive_time(0, 45, 500)
        collision_avoidance() # check if collision free

def grab_ball():
    motor_grabber.run_target(200, 0, Stop.HOLD, False)  # be sure grabber is closed
    motor_arm.run_target(100, -270, Stop.HOLD)          # rotate arm down
    motor_grabber.run_target(200, -75, Stop.HOLD)       # open grabber
    robot.drive_time(-100, 0, 900)                      # drive back to get ball into reach of grabber
    # motor_grabber.run_target(200, 0, Stop.HOLD)         # close grabber
    motor_grabber.run_until_stalled(-200, Stop.HOLD, 50)
    motor_arm.run_target(100, 0, Stop.HOLD)             # rotate arm back up
    motor_grabber.run_target(200, -75, Stop.HOLD)       # open grabber
    motor_grabber.run_target(200, 0, Stop.COAST)        # close grabber

    brick.display.image(ImageFile.THUMBS_UP)
    brick.sound.file(SoundFile.FANFARE)
    global ball_count
    ball_count += 1
    return

def check_ball():
    # if color_sensor_floor.color() == Color.RED:
    if color_sensor_floor.color() != calibration_surface:
        robot.stop()
        grab_ball()

def random_negate():
    return [-1,1][random.randrange(2)]

def check_container_full():
    return color_sensor_ramp.color() != calibration_ramp

global last_direction_change
last_direction_change = 0

# reset axes
motor_arm.run_until_stalled(100, Stop.COAST, 30)
motor_arm.reset_angle(0)
motor_grabber.run_until_stalled(100, Stop.COAST, 30)
motor_grabber.reset_angle(0)
calibration_surface = color_sensor_floor.color()
calibration_ramp = color_sensor_ramp.color()

while ball_count < 4:
    global last_direction_change

    collision_avoidance()
    check_ball()
    if check_container_full():
        break

    # run every 1s
    if watch.time() - last_direction_change > random_direction_change_interval:
        last_direction_change = watch.time()
        random_direction = random.randint(0, 91)
        robot.drive_time(drive_speed, random_negate() * rotation_speed, (random_direction / rotation_speed) * 1000)
        brick.display.clear()
    robot.drive(drive_speed, 0)



    # brick.display.clear()
    # brick.display.text(ultrasonic.presence(), (0, 20))
    # wait(200)
    # brick.display.text(ultrasonic.distance(), (0, 40))
    # brick.display.text(color_sensor_floor.rgb(), (0,10))
    # brick.display.text(color_sensor_floor.reflection(), (0,20))
    # brick.display.text(color_sensor_floor.color(), (0,30))
    # print(ultrasonic.presence())
    # print(ultrasonic.distance())
    # ultrasonic2.distance()
    # wait(100)
