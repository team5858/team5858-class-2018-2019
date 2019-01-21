"""
Move the ball-intake backwards
"""
from wpilib.command import Command
import subsystems


class BallIntake(Command):
    """BallIntake backwards"""

    def __init__(self):
        super().__init__("Make ball go backwards")

        self.requires(subsystems.ROBOT.ball_intake)

    def initialize(self):
        print("ballbackward" + str(self))
        subsystems.ROBOT.ball_intake.backward()

    def isFinished(self):
        return True
