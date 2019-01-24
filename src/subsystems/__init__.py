"""

***** DRIVETRAIN *****

The robot's driving base. There are 2 gear boxes on each side. Each
box has 2 motors. Each box has a built in encoder?

  4 [CAN OUT] Motors, 2 per side. 2 leaders, two followers.
  2 [PNU OUT] Double-pistons for gear shifting
  2 [DIO IN]  Motor encoders (one per gear box)
  
***** ELEVATOR *****

An 'L' shaped lifting platform. The lower (horizontal) leg raises
and lowers. Two motors are used to raise/lower. There are two switches,
one on top and bottom, to detect the limits. One of the motors uses
an encoder to detect position. This encoder is connected directly to
the TalonSRX.

There is a bicycle brake to hold the platform at the desired position.
This brake is controlled by a single-piston (with spring return).

The lower (horizontal) leg also pivots between full-up
and full-down (90 degrees). A double-piston raises or lowers the leg.

  2 [CAN OUT] Motors set as leader/follower (one built-in encoder)
  1 [PNU OUT] Single piston for the brake
  1 [PNU OUT] Double piston for the leg lift 

***** CARGO HANDLER *****

The  lower (horizontal) leg of the ELEVATOR holds 4 wheels for pulling/pushing 
balls. Two motors control theses wheels.

The lower (horizontal) leg holds a pop-out mechanism to push hatches. The pop-out
is a single-piston (with spring return).

  2 [CAN OUT] Motors set as leader/follower
  1 [PNU OUT] Single piston for pop-out
  
  
***** Totals *****

  8 CAN Motors (at least one TalonSRX to read an encoder for the elevator)
  3 PNU Double pistons (6 total pneumatic channels)
  2 PNU Single pistons (2 total pneumatic channels)
  2 DIO Channels for motor encoders

"""

# These are the singletons of the subsystems ... here for
# easy access by commands.

LEDS = None
DRIVETRAIN = None
VACUUM = None
BALL_INTAKE = None

JOYSTICK = None
