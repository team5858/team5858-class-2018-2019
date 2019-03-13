import wpilib
from wpilib.command.subsystem import Subsystem
import subsystems
from ctre import VictorSPX
from ctre import TalonSRX
from wpilib import SmartDashboard
from ctre import FeedbackDevice
from wpilib import Preferences
from ctre import ControlMode
from wpilib import DoubleSolenoid
from commands.ball_z import BallZ
from wpilib.doublesolenoid import DoubleSolenoid
from utility.set_motor import set_motor

CAN_ELBOW_LEADER = 7 #3 on practice bot
CAN_ELBOW_FOLLOWER = 10 #2 on practice bot
CAN_BALL_INTAKE = 3 #7 on practice bot

class Payload(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):
        super().__init__("Payload")
        # TODO Two limit switches on the leader
        self.prefs = Preferences.getInstance()

        self.elbowleader = TalonSRX(CAN_ELBOW_LEADER)
        set_motor(self.elbowleader, TalonSRX.NeutralMode.Brake, False)
        self.elbowleader.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)
        self.elbowleader.setSelectedSensorPosition(0, 0, 0)
        self.elbowleader.selectProfileSlot(0, 0)
        self.elbowleader.setSensorPhase(True)

        self.elbowfollower = VictorSPX(CAN_ELBOW_FOLLOWER)
        set_motor(self.elbowfollower, VictorSPX.NeutralMode.Brake, False)
        self.elbowfollower.follow(self.elbowleader)

        self.baller = TalonSRX(CAN_BALL_INTAKE)
        set_motor(self.baller, TalonSRX.NeutralMode.Brake, False)

        self.elbow_zero = False

        self.DS = DoubleSolenoid(2, 3)
        self.set_values()

    def initDefaultCommand(self):
        self.setDefaultCommand(BallZ())

    def set_wheels_speed(self,speed):
        self.baller.set(ControlMode.PercentOutput, speed)
        #print(speed)

    def hatch_punch_out(self):
        subsystems.SERIAL.fire_event('Punch It')
        self.DS.set(DoubleSolenoid.Value.kForward)

    def hatch_punch_in(self):
        self.DS.set(DoubleSolenoid.Value.kReverse)
    
    def set_position(self,pos):
        if self.elbow_zero:
            self.elbowleader.set(mode=ControlMode.MotionMagic, demand0=pos)
        else:
            print("Elbow Not Set")

    def set_speed(self, speed):
        self.elbowleader.set(mode=ControlMode.PercentOutput, demand0=speed)

    def set_values(self):
        self.elbowleader.config_kP(0, 0.8, 0)
        self.elbowleader.config_kI(0, 0.0, 0)
        self.elbowleader.config_kD(0, 0.0, 0)
        self.elbowleader.configMotionCruiseVelocity(int(200), 0)
        self.elbowleader.configMotionAcceleration(int(200), 0)

    def get_position(self):
        return self.elbowleader.getSelectedSensorPosition(0)

    def check_for_zero(self):
        if not self.elbow_zero:
            if self.elbowleader.isRevLimitSwitchClosed():
                self.elbowleader.setSelectedSensorPosition(0, 0, 0)
                self.elbow_zero = True

    def publish_data(self):
        #print(self.elbowleader.getSelectedSensorPosition(0))
        SmartDashboard.putNumber("elbowPosition",self.elbowleader.getSelectedSensorPosition(0))
        #SmartDashboard.putNumber("elbowVelocity", self.elbowleader.getSelectedSensorVelocity(0))
        #SmartDashboard.putNumber("elbowCurrent", self.elbowleader.getOutputCurrent())
        #SmartDashboard.putNumber("elbowOutput", self.elbowleader.getMotorOutputPercent())
