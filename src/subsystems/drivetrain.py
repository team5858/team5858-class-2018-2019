"""
Drivetrain subsystem.

#talon srx - leader
#4 and 5
#4 left, 5 right

#victor spx - follower
#9 and 10
#9 left, 10 right

"""

from ctre.wpi_talonsrx import WPI_TalonSRX
from ctre.wpi_victorspx import WPI_VictorSPX
from wpilib.command.subsystem import Subsystem
from wpilib.drive import DifferentialDrive

from commands.drive import Drive


class Drivetrain(Subsystem):
    """Functions for the drivetrain"""

    def __init__(self):
        super().__init__("Drivetrain")

        self.leftfollower = WPI_VictorSPX(9)
        self.leftleader = WPI_TalonSRX(4)
        self.rightfollower = WPI_VictorSPX(10)
        self.rightleader = WPI_TalonSRX(5)
        self.leftfollower.follow(self.leftleader)
        self.rightfollower.follow(self.rightleader)

        self.drive = DifferentialDrive(self.leftleader, self.rightleader)

    def stickdrive(self, stick):
        """set the motors based on the user inputs"""
        self.drive.arcadeDrive(stick.getY(), stick.getRawAxis(4))

    def initDefaultCommand(self):
        self.setDefaultCommand(Drive())
