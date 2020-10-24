#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

Left_Motor = Motor (Port.B)
Right_Motor = Motor (Port.C)
Front_Motor = Motor (Port.A)
Back_Motor = Motor (Port.D)
Wheel_Diameter = 38.6
TrackWidth = 126

def Reset_Motors (angle_val) :
    Left_Motor.reset_angle(angle_val)
    Right_Motor.reset_angle(angle_val)
    Front_Motor.reset_angle(angle_val)
    Back_Motor.reset_angle(angle_val)

def class Robot :
    Chassis = DriveBase (Left_Motor, Right_Motor, Wheel_Diameter, TrackWidth)
    
    def MoveDistance (speed, distance):
        MotorTurnAngle = (360 * distance) / (pi * Wheel_Diameter)
        Reset_Motors (0)
        while (Left_Motor.angle()+Right_Motor.angle())/2 < MotorTurnAngle
            Chassis.drive(speed, 0)
        Chassis.stop ()
    
    def OdoTurn (angle_val, whichMotor, direction):
        MotorTurnAngle = TrackWidth/Wheel_Diameter
        TurnAngle = angle_val * MotorTurnAngle
        set_Motor = Motor (Port.whichMotor)
        Reset_Motors ()
        set_Motor.run_target(100, TurnAngle, Stop.BREAK, True)

def linesquare () :



