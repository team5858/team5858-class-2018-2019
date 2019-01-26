import wpilib
from wpilib.command.subsystem import Subsystem


class HatchesBalls(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):

        super().__init__("LEDs")

        self._led_red = wpilib.DigitalOutput(DIO_LED_RED)
        self._led_green = wpilib.DigitalOutput(DIO_LED_GREEN)

    def elevator_up_down(self,direction):
        pass