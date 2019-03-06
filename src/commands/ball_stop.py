"""
Stop the ball intake
"""

from wpilib.command import Command
import subsystems


class BallStop(Command):
    """Ball-intake stop"""

    def __init__(self):
        super().__init__("Make ball stop")

        self.requires(subsystems.PAYLOAD)

    def initialize(self):
        subsystems.PAYLOAD.set_speed(0.0)

    def isFinished(self):
        return True
