"""
The status/test LEDs attached to the DIO pins
"""

import wpilib
from wpilib.command.subsystem import Subsystem

# TODO move these IDs to __init__

DIO_LED_RED = 0
DIO_LED_GREEN = 2


class LEDs(Subsystem):
    """
    Control for the diagnostics LEDs.
    """

    def __init__(self):

        super().__init__("LEDs")

        self._led_red = wpilib.DigitalOutput(DIO_LED_RED)
        self._led_green = wpilib.DigitalOutput(DIO_LED_GREEN)

    def set_red(self, state):
        """Set the state of the RED led"""
        self._led_red.set(state)

    def set_green(self, state):
        """Set the state of the GREEN led"""
        self._led_green.set(state)
