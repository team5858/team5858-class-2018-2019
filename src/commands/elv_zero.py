from wpilib.command import Command
import subsystems

class elv_zero(Command):

    def __init__(self):
        super().__init__("")

        self.requires(subsystems.ELEVATOR)

    def initialize(self):
        subsystems.ELEVATOR.elevator_zero = False

    def execute(self):
        subsystems.ELEVATOR.check_for_zero()
        # pass

    def isFinished(self):
        # This is always running
        return False
