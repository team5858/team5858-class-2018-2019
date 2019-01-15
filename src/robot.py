#!/usr/bin/env python3

"""
Main program for 2019
"""

from commands.autonomous import AutonomousProgram

import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot

from subsystems import leds

import oi

class HurricaneRobot(CommandBasedRobot):
    """
    The robot starts here. The code here sets up the subsystems and mode commands.
    """

    def robotInit(self):
        """
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        """

        # All commands can get access to this object with "getRobot()"
        Command.getRobot = lambda x=0: self

        self.leds = leds.LEDs()

        self.autonomous_program = AutonomousProgram()

        #self.teleop_program = TeleopProgram()

        """
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        """
        self.joystick = oi.get_joystick()

    def autonomousInit(self):
        """
        You should call start on your autonomous program here. You can
        instantiate the program here if you like, or in robotInit as in this
        example. You can also use a SendableChooser to have the autonomous
        program chosen from the SmartDashboard.
        """

        self.autonomous_program.start()


if __name__ == "__main__":
    wpilib.run(HurricaneRobot)
