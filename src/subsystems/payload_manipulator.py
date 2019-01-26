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

    def move_ball(self,direction):
        pass

    def punch_hatch(self,direction):
        pass

    def lift_up_down(self,direction):
        pass