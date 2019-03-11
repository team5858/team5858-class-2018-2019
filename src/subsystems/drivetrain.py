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
import wpilib
from wpilib.command.subsystem import Subsystem
from wpilib.doublesolenoid import DoubleSolenoid
from wpilib.drive import DifferentialDrive

from commands.drive import Drive
import subsystems
from utility.set_motor import set_motor

# TODO move these IDs to the __init__
CAN_LEFT_LEADER = 4
CAN_LEFT_FOLLOWER = 1  #10 on practice bot
CAN_RIGHT_LEADER = 6  #5 on practice bot
CAN_RIGHT_FOLLOWER = 2  #9 on practice bot
PNU_LEFT_HIGH = 1
PNU_LEFT_LOW = 2
PNU_RIGHT_HIGH = 3
PNU_RIGHT_LOW = 4

class Drivetrain(Subsystem):
    """Functions for the drivetrain"""

    def __init__(self):
        super().__init__("Drivetrain")

        self.leftleader = WPI_TalonSRX(CAN_LEFT_LEADER)
        set_motor(self.leftleader, WPI_TalonSRX.NeutralMode.Brake, False)

        self.leftfollower = WPI_VictorSPX(CAN_LEFT_FOLLOWER)
        set_motor(self.leftfollower, WPI_VictorSPX.NeutralMode.Brake, False)
        self.leftfollower.follow(self.leftleader)

        self.rightleader = WPI_TalonSRX(CAN_RIGHT_LEADER)
        set_motor(self.rightleader, WPI_TalonSRX.NeutralMode.Brake, True)

        self.rightfollower = WPI_VictorSPX(CAN_RIGHT_FOLLOWER)
        set_motor(self.rightfollower, WPI_VictorSPX.NeutralMode.Brake, True)
        self.rightfollower.follow(self.rightleader)

        self.DS = wpilib.DoubleSolenoid(0, 1)

        self.drive = DifferentialDrive(self.leftleader, self.rightleader)
        self.drive.maxOutput = 1.0

    def stickdrive(self):
        """set the motors based on the user inputs"""
        stick = subsystems.JOYSTICK
        x = stick.getRawAxis(4)
        #if x > 0.3 or x < -0.3:
        #    self.drive.maxOutput = 1.0
        #else:
        #    self.drive.maxOutput = 1.0

        self.set_gear(stick.getZ() > 0.5)

        # print(x)
        y = stick.getY()
        self.drive.arcadeDrive(-x, y)

        #P = self.leftleader.getQuadraturePosition()
        #P2 = self.rightleader.getQuadraturePosition()
        #print (" Left " +str (P) + " Right " +str (P2))
        #P3 = self.leftleader.getMotorOutputVoltage()
        #P4 = self.rightleader.getMotorOutputVoltage()
        #print(" Left " + str(P3) + " Right " + str(P4))
        #P5 = self.leftleader.getOutputCurrent()
        #P6 = self.rightleader.getOutputCurrent()
        #print(" Left " + str(P5) + " Right " + str(P6))

    def initDefaultCommand(self):
        self.setDefaultCommand(Drive())

    def set_gear(self, direction):
        if direction:
            self.DS.set(DoubleSolenoid.Value.kForward)
            subsystems.SERIAL.fire_event('High gear')
        else:
            self.DS.set(DoubleSolenoid.Value.kReverse)
            subsystems.SERIAL.fire_event('Low gear')
