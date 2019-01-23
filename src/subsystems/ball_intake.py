"""
Ball intake system
"""

from ctre.wpi_victorspx import WPI_VictorSPX
from wpilib.command.subsystem import Subsystem

PWM_BALL_INTAKE = 1  # VictorSP Pro attached to PWM 1


class BallIntake(Subsystem):
    """Subsystem functions for the ball intake"""

    def __init__(self):
        super().__init__("BallIntake")
        self._ball_intake_motor = WPI_VictorSPX(1)

    def forward(self):
        """Move the ball intake forwards"""
        self._ball_intake_motor.speed(1.0)

    def backward(self):
        """Move the ball intake backwards"""
        self._ball_intake_motor.speed(-1.0)

    def stop(self):
        """Stop the ball intake"""
        self._ball_intake_motor.speed(0)
