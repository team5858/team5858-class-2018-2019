from wpilib.command import Command
import subsystems
class gear_shift(Command):

    def __init__(self,state):
        super().__init__("Change Gears")
        self._state = state
        self.requires(subsystems.DRIVETRAIN)

    def initialize(self):
        print("gear_change" + str(self))
        subsystems.DRIVETRAIN.set_gear(self._state)

    def isFinished(self):
        return True