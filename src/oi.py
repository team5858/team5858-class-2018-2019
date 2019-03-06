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

from commands import gear_shift
from commands.set_elv_pay import SetElvPay
from commands.hatch_punch import hatch_punch
from commands.set_elv_speed import SetElvSpeed
from commands.set_pay_speed import SetPaySpeed
from commands.ball_in import BallIn
from commands.ball_out import BallOut
from commands.ball_stop import BallStop
from commands.set_elv_pos import SetElvPosition

def get_joystick():
    """
    Assign commands to button actions, and publish your joysticks so you
    can read values from them later.
    """

    joystick = Joystick(0)
    joystick2 = Joystick(1)

    # TODO lots of commands to map here
    # TODO how are we going to count taps for position?

    # trigger = JoystickButton(joystick=joystick, buttonNumber=5)
    # trigger.whenPressed(gear_shift.gear_shift(True))
    # trigger.whenReleased(gear_shift.gear_shift(False))

    # rtrigger = JoystickButton(joystick=joystick, buttonNumber=6)
    # rtrigger.whenPressed(set_arm_pos.SetArmPosition(1024.0))
    # rtrigger.whenReleased(set_arm_pos.SetArmPosition(0.0))

    buttonB = JoystickButton(joystick=joystick, buttonNumber=2)
    buttonB.whenPressed(hatch_punch(True))
    buttonB.whenReleased(hatch_punch(False))

    buttonX = JoystickButton(joystick=joystick, buttonNumber=3)
    buttonX.whenPressed(SetElvPay(0, 200))

    buttonA = JoystickButton(joystick=joystick, buttonNumber=1)
    buttonA.whenPressed(SetElvPay(0, 3000))

    buttonL1 = JoystickButton(joystick=joystick, buttonNumber=5)
    buttonL1.whenPressed(BallIn())
    buttonL1.whenReleased(BallStop())

    buttonR1 = JoystickButton(joystick=joystick, buttonNumber=6)
    buttonR1.whenPressed(BallOut())
    buttonR1.whenReleased(BallStop())

    #button12 = JoystickButton(joystick=joystick2, buttonNumber=12)
    #button12.whenPressed(SetElvPay(0, 0))

    #buttonB = JoystickButton(joystick=joystick2, buttonNumber=2)
    #buttonB.whenPressed(SetElvSpeed(0.5))
    #buttonB.whenReleased(SetElvSpeed(0.0))

    #buttonA = JoystickButton(joystick=joystick2, buttonNumber=1)
    #buttonA.whenPressed(SetElvSpeed(-0.5))
    #buttonA.whenReleased(SetElvSpeed(0.0))

    buttonX = JoystickButton(joystick=joystick2, buttonNumber=3)
    buttonX.whenPressed(SetPaySpeed(0.7))
    buttonX.whenReleased(SetPaySpeed(0.0))

    buttonY = JoystickButton(joystick=joystick2, buttonNumber=4)
    buttonY.whenPressed(SetPaySpeed(-0.7))
    buttonY.whenReleased(SetPaySpeed(0.0))

    buttonA = JoystickButton(joystick=joystick2, buttonNumber=1)
    buttonA.whenPressed(SetElvSpeed(0.7))
    buttonA.whenReleased(SetElvPosition())

    buttonB = JoystickButton(joystick=joystick2, buttonNumber=2)
    buttonB.whenPressed(SetElvSpeed(-0.3))

    return joystick
