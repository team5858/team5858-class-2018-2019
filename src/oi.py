"""
Operator Interface -- map commands to buttons.
"""

from wpilib.buttons.joystickbutton import JoystickButton
from wpilib.joystick import Joystick

from commands.led_green import SetGreenLED
from commands.vacuum_trigger import VacuumTrigger


def get_joystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    joystick = Joystick(0)

    trigger = JoystickButton(joystick=joystick, buttonNumber=2)
    trigger.whenPressed(SetGreenLED(True))
    trigger.whenReleased(SetGreenLED(False))

    trigger = JoystickButton(joystick=joystick, buttonNumber=1)
    trigger.whenPressed(VacuumTrigger(True))
    trigger.whenReleased(VacuumTrigger(False))

    return joystick
