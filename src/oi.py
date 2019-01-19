"""
Operator Interface -- map commands to buttons.
"""

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

import commands.green_led_on

def get_joystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    joystick = Joystick(0)

    trigger = JoystickButton(joystick=joystick,buttonNumber= 2)
    trigger.whenPressed(commands.green_led_on.GreenLEDOn(True))
    trigger.whenReleased(commands.green_led_on.GreenLEDOn(False))

    trigger = JoystickButton(joystick=joystick, buttonNumber=1)
    trigger.whenPressed(commands.vacuum.VacuumTrigger (True))
    trigger.whenReleased(commands.vacuum.VacuumTrigger (False))




    return joystick
