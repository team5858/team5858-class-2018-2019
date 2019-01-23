"""
Control the green LED
"""

from wpilib.command import Command
import subsystems


class SetGreenLED(Command):
    """
    This command will set the GREEN LED state.
    """

    def __init__(self, state):
        super().__init__("Set the state of the green LED")

        self.requires(subsystems.LEDS)

        self._state = state

    def initialize(self):
        subsystems.LEDS.set_green(self._state)

    def isFinished(self):
        return True
