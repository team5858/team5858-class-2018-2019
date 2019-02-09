"""

***** DRIVETRAIN *****

The robot's driving base. There are 2 gear boxes on each side. Each
box has 2 motors. Each box has a built-in encoder that wires directly
to the leader motor controller.

Each gearbox has a high and low gear. A double-piston changes gears.

  4 [CAN OUT] Motors, 2 per side. 2 leaders, two followers. Built-in encoders
  2 [PNU OUT] Double-pistons for gear shifting

***** ELEVATOR *****

An 'L' shaped lifting platform. The lower (horizontal) leg is the "wrist". The
elevator raises and lowers the wrist. Two motors in leader/follower mode are used
to raise/lower. There are two switches, one on top and bottom, to detect the limits.
The leader motor uses an encoder to track position from the limits. This encoder
is connected directly to the TalonSRX. Elevator motors geared 65 to 1.

The wrist pivots between vertical and horizontal. Two motors in leader/follower mode
are used to pivot. There are two switches to detect the limits.
The leader motor uses an encoder to track position from the limits. This encoder
is connected directly to the TalonSRX. Wrist motors geared 1000 to 1.

  4 [CAN OUT] Motors set as leader/follower (two with built-in encoders)
  4 [DIO IN]  Limit switches

***** CARGO HANDLER *****

The wrist of the ELEVATOR holds 4 wheels for pulling/pushing
balls. One motor controls theses wheels.

The wrist holds a pop-out mechanism to push hatches. The pop-out
is two single-piston (with spring return).

  1 [CAN OUT] Motor
  2 [PNU OUT] Single piston for pop-out

***** Totals *****

 9 CAN Motors (at least four TalonSRX to read encoders)
  2 PNU Double pistons (4 total pneumatic channels)
  2 PNU Single pistons (2 total pneumatic channels)
  4 DIO Channels for limit switches

"""

# These are the singletons of the subsystems ... here for
# easy access by commands.

# TODO let's map all the CAN/PWM/PCM/etc IDs to variables here

LEDS = None
DRIVETRAIN = None
PAYLOAD = None
ELEVATOR = None
SERIAL = None
PIGEON = None

JOYSTICK = None
