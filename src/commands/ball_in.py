"""
Take a ball in
"""
from wpilib.command import Command
import subsystems


class BallIn(Command):
    """BallIntake IN"""

    def __init__(self):
        super().__init__("Take in a ball")

        self.requires(subsystems.PAYLOAD)

    def initialize(self):
        subsystems.PAYLOAD.wheels_in()

    def isFinished(self):
        return True
