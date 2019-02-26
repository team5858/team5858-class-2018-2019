from ctre import ControlMode
from ctre import FeedbackDevice
from ctre import TalonSRX
from ctre import VictorSPX
from wpilib import Preferences
from wpilib import SmartDashboard
import wpilib
from wpilib.command.subsystem import Subsystem

CAN_ELEVATOR_LEADER = 5
CAN_ELEVATOR_FOLLOWER = 9

def set_motor2(motor, brake, inverted):
    motor.enableCurrentLimit(False)
    motor.configPeakOutputForward(1, 0)
    motor.configPeakOutputReverse(-1, 0)
    motor.setNeutralMode(brake)
    motor.configOpenLoopRamp(0, 0)
    motor.setInverted(inverted)

class Elevator(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):

        super().__init__("Elevator")

        # Initializes the elevator Talon, put it as one for now
        self.elevatorleader = TalonSRX(CAN_ELEVATOR_LEADER)
        set_motor2(self.elevatorleader, TalonSRX.NeutralMode.Brake, False)
        self.elevatorleader.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)
        self.elevatorleader.setSelectedSensorPosition(0, 0, 0)
        self.elevatorleader.setSensorPhase(True)

        self.elevatorfollower = VictorSPX(CAN_ELEVATOR_FOLLOWER)
        set_motor2(self.elevatorfollower, TalonSRX.NeutralMode.Brake, False)
        self.elevatorfollower.follow(self.elevatorleader)

        # The preference table is used to get values to the code while the
        # robot is running, useful
        self.prefs = Preferences.getInstance()
        # for tuning the PIDs and stuff

        self.set_values()

    def set_position(self, position):
        position = self.prefs.getFloat("Elevator Position", 0)
        self.elevatorleader.set(ControlMode.MotionMagic, position)

    def elevator_speed(self, speed):
        self.elevatorleader.set(ControlMode.PercentOutput, speed)

    def set_values(self):
        # This will set the PIDs, velocity, and acceleration, values from the
        # preference table so we can tune them easily
        self.elevatorleader.config_kP(0, self.prefs.getFloat("Elevator P", 0.1), 0)
        self.elevatorleader.config_kI(0, self.prefs.getFloat("Elevator I", 0.0), 0)
        self.elevatorleader.config_kD(0, self.prefs.getFloat("Elevator D", 0.0), 0)
        self.elevatorleader.configMotionCruiseVelocity(
            int(self.prefs.getInt("Elevator Velocity", 1024)), 0)
        self.elevatorleader.configMotionAcceleration(
            int(self.prefs.getInt("Elevator Acceleration", 1024)), 0)

    def publish_data(self):
        # This will print the position and velocity to the smartDashboard
        SmartDashboard.putNumber("Elevator Position", self.elevatorleader.getSelectedSensorPosition(0))
        SmartDashboard.putNumber("Elevator Velocity", self.elevatorleader.getSelectedSensorVelocity(0))
        SmartDashboard.putNumber("Elevator Current", self.elevatorleader.getOutputCurrent())
        SmartDashboard.putNumber("Elevator Output", self.elevatorleader.getMotorOutputPercent())

    def get_position(self):
        return self.elevatorleader.getSelectedSensorPosition(0)




