#!/usr/bin/env python3

"""
Main program for 2019
"""

from commandbased import CommandBasedRobot
import wpilib

from commands.autonomous import AutonomousProgram
import oi
import subsystems
from subsystems.ball_intake import BallIntake
from subsystems.drivetrain import Drivetrain
from subsystems.leds import LEDs
from subsystems.vacuum import Vacuum


class HurricaneRobot(CommandBasedRobot):
    """
    The robot starts here. The code here sets up the subsystems and mode commands.
    """

    def __init__(self):
        super().__init__()
        self.leds = None
        self.drivetrain = None
        self.vacuum = None
        self.ball_intake = None
        self.joystick = None

    def robotInit(self):
        """
        This is a good place to set up your subsystems and anything else that
        you will need to access later.
        """

        # All commands can get access to the subsystems here
        subsystems.ROBOT = self

        self.leds = LEDs()
        self.drivetrain = Drivetrain()
        self.vacuum = Vacuum()
        self.ball_intake = BallIntake()

        """
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        """
        self.joystick = oi.get_joystick()

    def autonomousInit(self):
        """
        Called to start the automomous command
        """

        autonomous_program = AutonomousProgram()
        autonomous_program.start()


if __name__ == "__main__":
    wpilib.run(HurricaneRobot)
