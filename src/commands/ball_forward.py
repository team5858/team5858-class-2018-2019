"""
Command to move the ball-intake forwards
"""
from wpilib.command import Command

import subsystems


class BallIntake(Command):
    """Ball-intake forwards"""

    def __init__(self):
        super().__init__("Make ball go forwards")

        self.requires(subsystems.ROBOT.ball_intake)

    def initialize(self):
        print("ballforward" + str(self))
        subsystems.ROBOT.ball_intake.forward()

    def isFinished(self):
        return True
