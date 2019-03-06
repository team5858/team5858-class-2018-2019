""""
Take a ball in
"""
from wpilib.command import Command
import subsystems


class SetArmPosition(Command):
    """BallIntake IN"""

    def __init__(self):
        super().__init__("set_arm_position")

        self.requires(subsystems.PAYLOAD)

    def initialize(self):
        subsystems.PAYLOAD.set_values()
        subsystems.PAYLOAD.set_position(subsystems.PAYLOAD.get_position())

    def isFinished(self):
        return True

