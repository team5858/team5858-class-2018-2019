from wpilib.command import Command
import subsystems

class hatch_punch(Command):
    """Shift gears"""

    def __init__(self, out):
        super().__init__("Punch Out")
        self._out = out
        self.requires(subsystems.PAYLOAD)

    def initialize(self):
        if self._out:
            subsystems.PAYLOAD.hatch_punch_out()
        else:
            subsystems.PAYLOAD.hatch_punch_in()

    def isFinished(self):
        return True
