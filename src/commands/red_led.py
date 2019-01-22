"""
Control the RED LED
"""

from wpilib.command import Command
import subsystems


class SetRedLED(Command):
    """
    This command will set the RED LEDs state.
    """

    def __init__(self, state):
        super().__init__("Set the state of the red LED")

        self.requires(subsystems.LEDS)

        self._state = state

    def initialize(self):
        subsystems.LEDS.set_red(self._state)

    def isFinished(self):
        return True

    # def execute(self):
    #    """Called repeatedly when this Command is scheduled to run"""
    #    pass

    # def end(self):
    #    """Called once after isFinished returns true"""
    #    return True

    # def interrupted(self):
    #    """Called when another command which requires one or more of the same
    #    subsystems is scheduled to run"""
    #    self.end()
