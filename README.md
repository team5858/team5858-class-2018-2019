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