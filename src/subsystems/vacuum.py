"""
Vacuum subsystem
"""

from wpilib.command.subsystem import Subsystem
from wpilib.victorsp import VictorSP

PWM_VACUUM = 6  # VictorSP Pro attached to PWM 6


class Vacuum(Subsystem):
    """Functions for the vacuum subsystem"""

    def __init__(self):
        super().__init__("Vacuum")
        self.vacmotor = VictorSP(PWM_VACUUM)

    def set_motor(self, on_off):
        """Set the vacuum on or off"""
        print('HELLO')
        if on_off:
            self.vacmotor.setSpeed(1)
        else:
            self.vacmotor.stopMotor()
