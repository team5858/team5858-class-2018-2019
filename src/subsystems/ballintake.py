from ctre.wpi_victorspx import WPI_VictorSPX

class BallIntake(Subsystem):

    def __init__(self):
        super().__init__("BallIntake")
        self.BallIntakeMotor = WPI_VictorSPX(1)

    def forward(self):
        self.BallIntakeMotor.speed(1.0)

    def backward(self):
        self.BallIntakeMotor.speed(-1.0)

    def stop(self):
        self.BallIntakeMotor.speed(0)