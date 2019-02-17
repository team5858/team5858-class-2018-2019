import wpilib
from wpilib.command.subsystem import Subsystem
import subsystems
from ctre.wpi_talonsrx import WPI_TalonSRX
from wpilib import SmartDashboard
from ctre import FeedbackDevice
from wpilib import Preferences
from ctre import ControlMode
from commands.ball_z import BallZ
from  wpilib.doublesolenoid import DoubleSolenoid

CAN_ELBOW_LEADER = 3
CAN_ELBOW_FOLLOWER = 2
CAN_BALL_INTAKE = 7

def set_motor2(motor, brake, inverted):
    motor.enableCurrentLimit(False)
    motor.configPeakOutputForward(1, 0)
    motor.configPeakOutputReverse(-1, 0)
    motor.setNeutralMode(brake)
    motor.configOpenLoopRamp(0, 0)
    motor.setInverted(inverted)

class Payload(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):
        super().__init__("Payload")
        # TODO Two limit switches on the leader
        self.prefs = Preferences.getInstance()

        self.elbowleader = WPI_TalonSRX(CAN_ELBOW_LEADER)
        set_motor2(self.elbowleader, WPI_TalonSRX.NeutralMode.Brake, False)
        self.elbowleader.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0, 0)
        self.elbowleader.setSelectedSensorPosition(0, 0, 0)
        self.elbowleader.selectProfileSlot(0, 0)
        self.elbowleader.setSensorPhase(True)

        self.elbowfollower = WPI_TalonSRX(CAN_ELBOW_FOLLOWER)
        set_motor2(self.elbowfollower, WPI_TalonSRX.NeutralMode.Brake, False)
        self.elbowfollower.follow(self.elbowleader)

        self.baller = WPI_TalonSRX(CAN_BALL_INTAKE)
        set_motor2(self.baller, WPI_TalonSRX.NeutralMode.Brake, False)

        self.DS = wpilib.DoubleSolenoid(2, 3)

        self.set_values()

    def initDefaultCommand(self):
        self.setDefaultCommand(BallZ())

    def set_wheels_speed(self,speed):
        self.baller.set(speed)

    def hatch_punch_out(self):
        subsystems.SERIAL.fire_event('Punch It')
        self.DS.set(DoubleSolenoid.Value.kForward)

    def hatch_punch_in(self):
        self.DS.set(DoubleSolenoid.Value.kReverse)
    
    def set_position(self,pos):
        self.elbowleader.set(mode = ControlMode.MotionMagic, demand0=pos)

    def set_values(self):
        self.elbowleader.config_kP(0, self.prefs.getFloat("Elbow P", 0.1), 0)
        self.elbowleader.config_kI(0, self.prefs.getFloat("Elbow I", 0), 0)
        self.elbowleader.config_kD(0, self.prefs.getFloat("Elbow D", 0), 0)
        self.elbowleader.configMotionCruiseVelocity(int(self.prefs.getFloat("ElbowVel", 1024)), 0)
        self.elbowleader.configMotionAcceleration(int(self.prefs.getFloat("ElbowAcc", 1024)), 0)

    def get_position(self):
        return self.elbowleader.getSelectedSensorPosition(0)

    def print_position(self):
        SmartDashboard.putNumber("elbowposition",self.elbowleader.getSelectedSensorPosition(0))
        SmartDashboard.putNumber("elbowVelocity", self.elbowleader.getSelectedSensorVelocity(0))
