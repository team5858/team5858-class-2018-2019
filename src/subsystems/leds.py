"""
The status/test LEDs attached to the DIO pins
"""

import wpilib
from wpilib.command.subsystem import Subsystem

class LEDs(Subsystem):
    """
    Control for the LEDs.
    """

    def __init__(self):

        super().__init__("LEDs")

        self._led_red   = wpilib.DigitalOutput(0)  # Red LED hooked up to Digital Output 0
        self._led_green = wpilib.DigitalOutput(2)  # Green LED hooked up to Digital Output 2

    def set_red(self,state):
        """Set the state of the RED led"""
        self._led_red.set(state)

    # TODO Add setter for GREEN LED
    