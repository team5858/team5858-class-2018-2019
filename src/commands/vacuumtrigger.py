

from wpilib.command import Command

from wpilib.command.waitcommand import WaitCommand

class Drive(Command):


    def __init__(self):
        super().__init__("Drive")

        self.requires(self.getRobot().drivetrain)

    def initialize(self):
       pass

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return False
    def execute(self):
        "Called repeatedly when this Command is scheduled to run  "
        self.robot.drivetrain.tankDriveJoystick(self.robot.oi.getJoystick())

     def end(self):
         self.robot.drivetrain.stop()

     def interrupted(self):
         self.end()




