# The FRC 2019 Competition Robot

## robot.py and oi.py

The `robot.py` is the entry point. This code builds all the subsystem singletons, maps commands to
the joystick (through `oi.py`), and configures the mode-commands for TELEOP and AUTONOMOUS.

The `oi.py` maps one-shot commands to the joystick buttons.

## subsystems

The `subsystems` package contains all the singleton classes for the various parts of the robot.
The package `__init__.py` holds references to the singletons for access by other code.

For instance:

```python
import subsystems
subsystems.BALL_INTAKE.stop()
```

### ball_intake.BallIntake

A motor for pushing or pulling a ball.

### drivetrain.Drivetrain

Two leader motors (TalonSRX) and two follower motors (VictorSPX).

### leds.LEDs

A red and a green hooked up to DIO pins.

### vacuum.Vacuum

A motor for the vacuum.

## Commands

### Groups
  - autonomous.AutonomousProgram : Flash red LED 4 times
  
### Individuals
  - ball_backward.BallBackward
  - ball_forward.BallForward
  - ball_stop.BallStop
  - drive.Drive
  - led_green.SetGreenLED(state)
  - red_led.SetSetLED(state)
  - vacuum_trigger.VacuumTrigger(state)
  
From Chris
```
so you'll have drivetrain obviously, the ball intake (the green grippy wheels on an axle), the hatch-remover (just two pneumatic pistons), the elevator (lifts the whole ball intake / hatch-remover up into the air), and the "payload" controller, the thing that the hatch-pickup/ball intake is connected to.

you'll need some PID + probably limit switches for the elevator and the payload controller (going to an angle and staying there, etc), i'm looking at putting some small limit switches onto the hatch pickup part so you don't try to keep going when you get to the ground

tophercantrell [3:51 PM]
that'll be great

chris.dail [3:51 PM]
In theory you could do it with PID and know how many pulses to go and all

tophercantrell [3:52 PM]
i like the switches
safest way to go

chris.dail [3:52 PM]
well you'll want to do the PID to so you can adjust to different angles and whatnot
the hatch pickup has to be able to get to the ground or upright
but the limit switches are a good hard stop safety addition

tophercantrell [3:53 PM]
Yep! We need to whip up a good systems diagram. Show motors and sensors and whatnot

chris.dail [3:53 PM]
right yeah
```