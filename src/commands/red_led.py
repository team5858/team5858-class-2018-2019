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
