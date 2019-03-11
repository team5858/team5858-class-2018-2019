"""
Take a ball in
"""
from wpilib.command import Command
import subsystems

class BallZ(Command):
    """BallIntake IN"""

    def __init__(self):
        super().__init__("Take in a ball")

        self.requires(subsystems.PAYLOAD)

    def initialize(self):
        subsystems.PAYLOAD.elbow_zero = False

    def execute(self):
        # subsystems.PAYLOAD.set_wheels_speed(subsystems.JOYSTICK.getZ())
        subsystems.PAYLOAD.check_for_zero()
        subsystems.PAYLOAD.publish_data()
        pass

    def isFinished(self):
        # This is always running
        return False
