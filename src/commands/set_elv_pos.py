""""
Take a ball in
"""
from wpilib.command import Command
import subsystems


class SetElvPosition(Command):
    """BallIntake IN"""

    def __init__(self):
        super().__init__("set_arm_position")

        self.requires(subsystems.PAYLOAD)

    def initialize(self):
        subsystems.ELEVATOR.set_values()
        subsystems.ELEVATOR.set_position(subsystems.ELEVATOR.get_position())

    def isFinished(self):
        return True
