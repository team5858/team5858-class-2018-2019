import wpilib
from wpilib.command.subsystem import Subsystem
import subsystems
from ctre.wpi_talonsrx import WPI_TalonSRX
CAN_ELBOW_LEADER = 3
CAN_ELBOW_FOLLOWER = 2
CAN_BALL_INTAKE = 7

def set_motor2(motor, brake):
    motor.enableCurrentLimit(False)
    motor.configPeakOutputForward(1, 0)
    motor.configPeakOutputReverse(-1, 0)
    motor.setNeutralMode(brake)
    motor.configOpenLoopRamp(0, 0)

class Payload(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):
        super().__init__("Payload")
        # TODO Two motors ... one leader, one follower
        # TODO Two limit switches on the follower

        self.elbowleader = WPI_TalonSRX(CAN_ELBOW_LEADER)
        self.elbowleader.setInverted(False)
        set_motor2(self.elbowleader, WPI_TalonSRX.NeutralMode.Brake)

        self.elbowfollower = WPI_TalonSRX(CAN_ELBOW_FOLLOWER)
        self.elbowfollower.setInverted(False)
        set_motor2(self.elbowfollower, WPI_TalonSRX.NeutralMode.Brake)

    def wheels_in(self):
        # TODO Spin motors to bring ball in
        subsystems.SERIAL.fire_event('Wheels In')

    def wheels_out(self):
        # TODO Spin motors to push ball out
        subsystems.SERIAL.fire_event('Wheels Out')

    def wheels_stop(self):
        # TODO Stop motors
        subsystems.SERIAL.fire_event('Wheels Stop')

    def hatch_punch_out(self):
        # TODO send air to piston
        pass

    def hatch_punch_in(self):
        # TODO turn off air to piston
        pass
    
    def elbow_down(self):
        self.elbowleader.speed = 1

    def elbow_up(self):
        self.elbowleader.speed = 0
