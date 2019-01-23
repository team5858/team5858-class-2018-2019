"""
Command to move the ball-intake forwards
"""

from wpilib.command import Command
import subsystems


class BallForward(Command):
    """Ball-intake forwards"""

    def __init__(self):
        super().__init__("Make ball go forwards")

        self.requires(subsystems.BALL_INTAKE)

    def initialize(self):
        print("ballforward" + str(self))
        subsystems.BALL_INTAKE.forward()

    def isFinished(self):
        return True
