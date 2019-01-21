"""
Stop the ball intake
"""
from wpilib.command import Command

import subsystems


class BallIntake(Command):
    """Ball-intake stop"""

    def __init__(self):
        super().__init__("Make ball stop")

        self.requires(subsystems.ROBOT.ball_intake)

    def initialize(self):
        print("ballstop" + str(self))
        subsystems.ROBOT.ball_intake.stop()

    def isFinished(self):
        return True
