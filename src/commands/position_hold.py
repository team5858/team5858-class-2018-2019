
from wpilib.command import Command
import subsystems

class SetElvPay (Command):
    """stow arm """

    def __init__(self):
        super().__init__("stow arm")

        self.requires(subsystems.PAYLOAD)
        self.requires(subsystems.ELEVATOR)

    def initialize(self):
        subsystems.PAYLOAD.set_values()
        subsystems.PAYLOAD.set_position(subsystems.PAYLOAD.get_position())
        subsystems.ELEVATOR.set_values()
        subsystems.ELEVATOR.set_position(subsystems.ELEVATOR.get_position())

    def execute(self):
        subsystems.ELEVATOR.publish_data()
        subsystems.PAYLOAD.publish_data()

    def isFinished(self):
        return True
