"""
Continuous driving
"""

from wpilib.command import Command
import subsystems


class Drive(Command):
    """Drive the robot from the joystick"""

    def __init__(self):
        super().__init__("Drive")

        self.requires(subsystems.DRIVETRAIN)

    def execute(self):
        subsystems.DRIVETRAIN.stickdrive()

    def isFinished(self):
        # This is always running
        return False
