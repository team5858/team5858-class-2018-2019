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

CAN_LEFT_LEADER = 2  # TalonSRX with CAN ID 4
CAN_LEFT_FOLLOWER = 10  # VictorSPX with CAN ID 9
CAN_RIGHT_LEADER = 3  # TalonSRX with CAN ID 5
CAN_RIGHT_FOLLOWER = 9  # VictorSPX with CAN ID 10
PNU_LEFT_HIGH = 1
PNU_LEFT_LOW = 2
PNU_RIGHT_HIGH = 3
PNU_RIGHT_LOW = 4


def set_motor2(motor, brake):
    motor.enableCurrentLimit(False)
    motor.configPeakOutputForward(1, 0)
    motor.configPeakOutputReverse(-1, 0)
    motor.setNeutralMode(brake)
    motor.configOpenLoopRamp(0,0)

class Drivetrain(Subsystem):
    """Functions for the drivetrain"""


    def __init__(self):
        super().__init__("Drivetrain")

        self.leftleader = WPI_TalonSRX(CAN_LEFT_LEADER)
        self.leftleader.setInverted(False)
        set_motor2(self.leftleader,WPI_TalonSRX.NeutralMode.Brake )

        self.leftfollower = WPI_VictorSPX(CAN_LEFT_FOLLOWER)
        self.leftfollower.setInverted(False)
        set_motor2(self.leftfollower,WPI_VictorSPX.NeutralMode.Brake)

        self.rightleader = WPI_TalonSRX(CAN_RIGHT_LEADER)
        set_motor2(self.rightleader,WPI_TalonSRX.NeutralMode.Brake )
        self.rightleader.setInverted(True)

        self.rightfollower = WPI_VictorSPX(CAN_RIGHT_FOLLOWER)
        set_motor2(self.rightfollower,WPI_VictorSPX.NeutralMode.Brake )
        self.rightfollower.setInverted(True)

        self.DS = wpilib.DoubleSolenoid(1,2)

        self.leftfollower.follow(self.leftleader)
        self.rightfollower.follow(self.rightleader)

        self.drive = DifferentialDrive(self.leftleader, self.rightleader)
        self.drive.maxOutput = 0.8

    def stickdrive(self):
        """set the motors based on the user inputs"""
        stick = subsystems.JOYSTICK
        x = stick.getRawAxis(4)
        y = stick.getY()
        self.drive.arcadeDrive(-(x*x*x),(y*y*y))
        P = self.leftleader.getQuadraturePosition()
        P2 = self.rightleader.getQuadraturePosition()
        print (" Left " +str (P) + " Right " +str (P2))
        P3 = self.leftleader.getMotorOutputVoltage()
        P4 = self.rightleader.getMotorOutputVoltage()
        #print(" Left " + str(P3) + " Right " + str(P4))
        P5 = self.leftleader.getOutputCurrent()
        P6 = self.rightleader.getOutputCurrent()
        #print(" Left " + str(P5) + " Right " + str(P6))
        #self.drive.arcadeDrive(-x, y)

    def initDefaultCommand(self):
        self.setDefaultCommand(Drive())

    def set_gear(self,direction):
        if direction:
            self.DS.set(DoubleSolenoid.Value.kForward)
        else:
            self.DS.set(DoubleSolenoid.Value.kReverse)

