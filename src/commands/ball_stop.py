"""
Stop the ball intake
"""

from wpilib.command import Command
import subsystems


class BallStop(Command):
    """Ball-intake stop"""

    def __init__(self):
        super().__init__("Make ball stop")

        self.requires(subsystems.BALL_INTAKE)

    def initialize(self):
        print("ballstop" + str(self))
        subsystems.BALL_INTAKE.stop()

    def isFinished(self):
        return True
