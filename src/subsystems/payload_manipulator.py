import wpilib
from wpilib.command.subsystem import Subsystem
import subsystems
from ctre.wpi_talonsrx import WPI_TalonSRX
from wpilib import SmartDashboard
from ctre import FeedbackDevice
from wpilib import Preferences
from ctre import ControlMode

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
        self.prefs = Preferences.getInstance()

        self.elbowleader = WPI_TalonSRX(CAN_ELBOW_LEADER)
        self.elbowleader.setInverted(False)
        set_motor2(self.elbowleader, WPI_TalonSRX.NeutralMode.Brake)
        self.elbowleader.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0, 0)
        self.elbowleader.setSelectedSensorPosition(0, 0, 0)
        self.elbowleader.selectProfileSlot(0, 0)
        self.elbowleader.setSensorPhase(True)

        self.elbowfollower = WPI_TalonSRX(CAN_ELBOW_FOLLOWER)
        self.elbowfollower.setInverted(False)
        set_motor2(self.elbowfollower, WPI_TalonSRX.NeutralMode.Brake)
        self.elbowfollower.follow(self.elbowleader)

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
    
    def set_position(self,pos):
        #self.elbowleader.set(pos)
        self.elbowleader.set(mode = ControlMode.MotionMagic, demand0=pos)
        #self.elbowleader.set(mode=WPI_TalonSRX.ControlMode.PercentOutput, demand0=pos)
        #self.elbowleader.set(mode=WPI_TalonSRX.ControlMode.Position, demand0=pos)

    def set_values(self):
        self.elbowleader.config_kP(0, self.prefs.getFloat("Elbow P", 0.1), 0)
        self.elbowleader.config_kI(0, self.prefs.getFloat("Elbow I", 0), 0)
        self.elbowleader.config_kD(0, self.prefs.getFloat("Elbow D", 0), 0)
        #self.elbowleader.configMotionCruiseVelocity(self.prefs.getFloat("Elbow Velocity", 100), 0)
        self.elbowleader.configMotionCruiseVelocity(int(self.prefs.getFloat("ElbowVel", 100)), 0)
        self.elbowleader.configMotionAcceleration(int(self.prefs.getFloat("ElbowAcc", 100)), 0)

    def get_position(self):
        return self.elbowleader.getSelectedSensorPosition(0)

    def print_position(self):
        SmartDashboard.putNumber("elbowposition",self.elbowleader.getSelectedSensorPosition(0))
        SmartDashboard.putNumber("elbowVelocity", self.elbowleader.getSelectedSensorVelocity(0))