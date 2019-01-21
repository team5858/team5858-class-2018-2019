

from wpilib.command import Command

import subsystems


class VacuumTrigger(Command):

    def __init__(self, state):
        super().__init__("Vacuum Trigger")
        self.requires(subsystems.ROBOT.vacuum)

        self._state = state

    def initialize(self):
        subsystems.ROBOT.vacuum.set_motor(self._state)

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return True
