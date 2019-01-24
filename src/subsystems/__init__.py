"""

***** DRIVETRAIN *****

The robot's driving base. There are 2 gear boxes on each side. Each
box has 2 motors. Each box has a built in encoder that wires directly
to the leader motor controller.

Each gearbox has a high and low gear. A double-piston changes gears.

  4 [CAN OUT] Motors, 2 per side. 2 leaders, two followers. Built-in encoders
  2 [PNU OUT] Double-pistons for gear shifting

***** ELEVATOR *****

An 'L' shaped lifting platform. The lower (horizontal) leg is the "wrist". The
elevator raises and lowers the wrist. Two motors in leader/follower mode are used
to raise/lower. There are two switches, one on top and bottom, to detect the limits.
The leader motor uses an encoder to track position from the limits. This encoder
is connected directly to the TalonSRX.

There is a bicycle brake to hold the platform at the desired position.
This brake is controlled by a single-piston (with spring return).

The wrist pivots between vertical and horizontal. Two motors in leader/follower mode
are used to pivot. There are two switches to detect the limits.
The leader motor uses an encoder to track position from the limits. This encoder
is connected directly to the TalonSRX.

  4 [CAN OUT] Motors set as leader/follower (two with built-in encoders)
  1 [PNU OUT] Single piston for the brake
  4 [DIO IN]  Limit switches

***** CARGO HANDLER *****

The  lower (horizontal) leg of the ELEVATOR holds 4 wheels for pulling/pushing
balls. Two motors control theses wheels.

The lower (horizontal) leg holds a pop-out mechanism to push hatches. The pop-out
is a single-piston (with spring return).

  2 [CAN OUT] Motors set as leader/follower
  1 [PNU OUT] Single piston for pop-out

***** Totals *****

 10 CAN Motors (at least four TalonSRX to read encoders)
  2 PNU Double pistons (4 total pneumatic channels)
  2 PNU Single pistons (2 total pneumatic channels)
  4 DIO Channels for limit switches

"""

# These are the singletons of the subsystems ... here for
# easy access by commands.

LEDS = None
DRIVETRAIN = None
VACUUM = None
BALL_INTAKE = None

JOYSTICK = None
