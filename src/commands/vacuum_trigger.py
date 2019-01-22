"""
Control the vacuum motor
"""

from wpilib.command import Command
import subsystems


class VacuumTrigger(Command):
    """Vacuum motor on or off"""

    def __init__(self, state):
        super().__init__("Vacuum Trigger")
        self.requires(subsystems.VACUUM)

        self._state = state

    def initialize(self):
        subsystems.VACUUM.set_motor(self._state)

    def isFinished(self):
        return True
