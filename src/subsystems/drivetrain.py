import wpilib
from wpilib.command.subsystem import Subsystem
from ctre.wpi_talonsrx import WPI_TalonSRX
from ctre.wpi_victorspx import WPI_VictorSPX
from wpilib.drive import DifferentialDrive
from commands.drive import Drive
class Drivetrains(Subsystem):


    def __init__(self):
        super().__init__("Drivetrains")

        self.leftfollower = WPI_VictorSPX(9)
        self.leftleader = WPI_TalonSRX(4)
        self.rightfollower = WPI_VictorSPX(10)
        self.rightleader = WPI_TalonSRX(5)
        self.leftfollower.follow(self.leftleader)
        self.rightfollower.follow(self.rightleader)

        self.drive = DifferentialDrive(self.leftleader, self.rightleader)

    def stickdrive(self,stick):
        self.drive.arcadeDrive(stick.getY(), stick.getRawAxis(4))
    def initDefaultCommand(self):
        self.setDefaultCommand(Drive())



