"""
Command to move the out
"""

from wpilib.command import Command
import subsystems


class BallOut(Command):
    """Ball-intake out"""

    def __init__(self):
        super().__init__("Make ball go out")

        self.requires(subsystems.PAYLOAD)

    def initialize(self):
        subsystems.PAYLOAD.set_wheels_speed(-1.0)

    def isFinished(self):
        return True
