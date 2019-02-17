"""
Take a ball in
"""
from wpilib.command import Command
import subsystems

class SetElvSpeed(Command):
    """stow arm """

    def __init__(self,speed):
        super().__init__("elv speed")

        self.requires(subsystems.ELEVATOR)
        self.speed = speed

    def initialize(self):
        subsystems.ELEVATOR.elevator_speed(self.speed)

    def isFinished(self):
        return True