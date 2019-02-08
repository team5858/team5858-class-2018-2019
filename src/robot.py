#!/usr/bin/env python3

"""
Main program for 2019
"""

from commandbased import CommandBasedRobot
import wpilib

import oi
import subsystems
from subsystems.drivetrain import Drivetrain
from subsystems.elevator import Elevator
from subsystems.leds import LEDs
from subsystems.payload_manipulator import Payload
from subsystems.serial_events import SerialEvent


class HurricaneRobot(CommandBasedRobot):
    """
    The robot starts here. This code sets up the subsystems, joystick triggers,
    and auto/teleop mode commands.
    """

    def robotInit(self):
        """
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        """

        # All commands can get access to the subsystems here
        subsystems.LEDS = LEDs()
        subsystems.DRIVETRAIN = Drivetrain()
        subsystems.ELEVATOR = Elevator()
        subsystems.PAYLOAD = Payload()
        subsystems.SERIAL = SerialEvent()

        """
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        """
        subsystems.JOYSTICK = oi.get_joystick()
        wpilib.CameraServer.launch()

    def autonomousInit(self):
        """
        Called to start the automomous command
        """

        subsystems.SERIAL.fire_event('Autonomous Mode')

    # WARNING. We need to implement the teleopInit just in case. The field *might* require that we do so (might kill
    # the autonomous command)


if __name__ == "__main__":
    wpilib.run(HurricaneRobot)
