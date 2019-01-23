"""
Move the ball-intake backwards
"""
from wpilib.command import Command
import subsystems


class BallBackward(Command):
    """BallIntake backwards"""

    def __init__(self):
        super().__init__("Make ball go backwards")

        self.requires(subsystems.BALL_INTAKE)

    def initialize(self):
        print("ballbackward" + str(self))
        subsystems.BALL_INTAKE.backward()

    def isFinished(self):
        return True
