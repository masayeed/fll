#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick


from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from macrolib import *

# Write your program here
Wheel_Diameter = 55.5
TrackWidth = 27.6

brick.sound.beep()
Left_Motor = Motor (Port.B)
Right_Motor = Motor (Port.C)
Front_Motor = Motor (Port.A)
Back_Motor = Motor (Port.D)

Robot = DriveBase (Left_Motor, Right_Motor, Wheel_Diameter, TrackWidth)

Reset_Motors (0)

Robot.MoveDistance (500, 50)
