"""
Take a ball in
"""
from wpilib.joystick import Joystick
from wpilib.command import Command
import subsystems


class BallZ(Command):
    """BallIntake IN"""

    def __init__(self):
        super().__init__("Take in a ball")

        self.requires(subsystems.PAYLOAD)
        self.joystick = Joystick(0)

    def execute(self):
        subsystems.PAYLOAD.set_wheels_speed(self.joystick.getZ())

    def isFinished(self):
        return False