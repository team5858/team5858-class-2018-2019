

from wpilib.command import Command

from wpilib.command.waitcommand import WaitCommand

class VacuumTrigger(Command):


    def __init__(self,state):
        super().__init__("VacuumTrigger")
        self.requires(self.getRobot().vacuum)

        self._state = state

    def initialize(self):
       self.getRobot ().vacuum.set_motor (self._state)

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return True




