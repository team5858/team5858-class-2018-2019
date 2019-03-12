""""
Take a ball in
"""
from wpilib.command import Command
import subsystems


class SetArmPosition(Command):
    """BallIntake IN"""

    def __init__(self, pos):
        super().__init__("set_arm_position")

        self.requires(subsystems.PAYLOAD)
        self.pos = pos

    def initialize(self):
        subsystems.PAYLOAD.set_values()
        subsystems.PAYLOAD.set_position(self.pos)

    def isFinished(self):
        return True

