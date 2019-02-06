"""
Operator Interface -- map commands to buttons.


TODO: map out these controls

  LeftStick:  turn left, right
  RightStick: forward, backwards

  ??:           Gear shift. Hold for low, release for high.
  HatUpDown:    Click N times for elevator level N.
  HatLeftRight: Click N times for wrist position N.
  ??:           Fine Tune. Hold to change hat switches to fine-tune position.
  ??:           Eject hatch. Push to eject.
  ??:           Ball-in. Hold to spin intake wheels.
  ??:           Ball-out. Hold to spin intake wheels.

  ??: Align to Rocket?
  ??: ALign to Hab?

"""

from wpilib.buttons.joystickbutton import JoystickButton
from wpilib.joystick import Joystick

from commands.gear_shift import gear_shift


def get_joystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    joystick = Joystick(0)

    # TODO lots of commands to map here
    # TODO how are we going to count taps for position?

    trigger = JoystickButton(joystick=joystick, buttonNumber=5)
    trigger.whenPressed(gear_shift(True))
    trigger.whenReleased(gear_shift(False))

    return joystick
