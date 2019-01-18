"""
Operator Interface -- map commands to buttons.
"""

from commands.crash import Crash

from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton

import commands.green_led_on

def get_joystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """[1]

    joystick = Joystick(0)

#    trigger = JoystickButton(joystick, Joystick.ButtonType.kTrigger) # A Button
    trigger = JoystickButton(joystick=joystick,buttonNumber= 2)
    trigger.whenPressed(commands.green_led_on.GreenLEDOn(True))
    trigger.whenReleased(commands.green_led_on.GreenLEDOn(False))


    return joystick
