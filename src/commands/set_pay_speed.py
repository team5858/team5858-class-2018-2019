"""
Take a ball in
"""
from wpilib.command import Command
import subsystems

class SetPaySpeed(Command):
    """set payload speed """

    def __init__(self,speed):
        super().__init__("pay speed")

        self.requires(subsystems.PAYLOAD)
        self.speed = speed

    def initialize(self):
        subsystems.PAYLOAD.set_speed(self.speed)

    def execute(self):
        subsystems.PAYLOAD.publish_data()

    def isFinished(self):
        return True
