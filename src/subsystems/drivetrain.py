"""
Drivetrain subsystem.

        Front
|O|               |O|
 |                 |
 |TSRX-4    TSRX-5 |
 |VSPX-9   VSPX-10 |
 |                 |
|O|               |O|
        Back
        
Motor Controllers:
  - Leaders:   TalsonSRX CAN:4,5
  - Followers: VictorSPX CAN:9,10

"""

from ctre.wpi_talonsrx import WPI_TalonSRX
from ctre.wpi_victorspx import WPI_VictorSPX
from wpilib.command.subsystem import Subsystem
from wpilib.drive import DifferentialDrive

from commands.drive import Drive
import subsystems
import wpilib
from wpilib.doublesolenoid import DoubleSolenoid

CAN_LEFT_LEADER = 4  # TalonSRX with CAN ID 4
CAN_LEFT_FOLLOWER = 9  # VictorSPX with CAN ID 9
CAN_RIGHT_LEADER = 5  # TalonSRX with CAN ID 5
CAN_RIGHT_FOLLOWER = 10  # VictorSPX with CAN ID 10
PNU_LEFT_HIGH = 1
PNU_LEFT_LOW = 2
PNU_RIGHT_HIGH = 3
PNU_RIGHT_LOW = 4


class Drivetrain(Subsystem):
    """Functions for the drivetrain"""

    def __init__(self):
        super().__init__("Drivetrain")

        self.leftleader = WPI_TalonSRX(CAN_LEFT_LEADER)
        self.leftleader.setInverted(True)
        self.leftfollower = WPI_VictorSPX(CAN_LEFT_FOLLOWER)
        self.leftfollower.setInverted(True)
        self.rightleader = WPI_TalonSRX(CAN_RIGHT_LEADER)
        self.rightfollower = WPI_VictorSPX(CAN_RIGHT_FOLLOWER)

        self.DS = wpilib.DoubleSolenoid(1,2)

        self.leftfollower.follow(self.leftleader)
        self.rightfollower.follow(self.rightleader)

        self.drive = DifferentialDrive(self.leftleader, self.rightleader)

    def stickdrive(self):
        """set the motors based on the user inputs"""
        stick = subsystems.JOYSTICK
        self.drive.arcadeDrive(stick.getRawAxis(4), -stick.getY())

    def initDefaultCommand(self):
        self.setDefaultCommand(Drive())

    def set_gear(self,direction):
        if direction:
            self.DS.set(DoubleSolenoid.Value.kForward)
        else:
            self.DS.set(DoubleSolenoid.Value.kReverse)

