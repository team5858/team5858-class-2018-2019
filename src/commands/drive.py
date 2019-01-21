"""
Continuous driving
"""
from wpilib.command import Command

from wpilib.command.waitcommand import WaitCommand

import subsystems


class Drive(Command):
    """Drive the robot from the joystick"""

    def __init__(self):
        super().__init__("Drive")

        self.requires(subsystems.ROBOT.drivetrain)

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return False

    def execute(self):
        "Called repeatedly when this Command is scheduled to run  "
        subsystems.ROBOT.drivetrain.stickdrive(subsystems.ROBOT.joystick)
