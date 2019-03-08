from ctre import ControlMode
from ctre import FeedbackDevice
from ctre import TalonSRX
from ctre import VictorSPX
from wpilib import Preferences
from wpilib import SmartDashboard
from wpilib.joystick import Joystick
from wpilib.buttons.joystickbutton import JoystickButton
import wpilib
from wpilib.command.subsystem import Subsystem
from commands.elv_zero import elv_zero
from commands.set_elv_pay import SetElvPay
from utility.set_motor import set_motor
CAN_ELEVATOR_LEADER = 5
CAN_ELEVATOR_FOLLOWER = 9

class Elevator(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):

        super().__init__("Elevator")

        # Initializes the elevator Talon, put it as one for now
        self.elevatorleader = TalonSRX(CAN_ELEVATOR_LEADER)
        set_motor(self.elevatorleader, TalonSRX.NeutralMode.Brake, False)
        self.elevatorleader.configSelectedFeedbackSensor(FeedbackDevice.QuadEncoder, 0, 0)
        self.elevatorleader.setSelectedSensorPosition(0, 0, 0)
        self.elevatorleader.setSensorPhase(False)

        self.elevatorfollower = VictorSPX(CAN_ELEVATOR_FOLLOWER)
        set_motor(self.elevatorfollower, TalonSRX.NeutralMode.Brake, False)
        self.elevatorfollower.follow(self.elevatorleader)

        # The preference table is used to get values to the code while the
        # robot is running, useful
        self.prefs = Preferences.getInstance()
        # for tuning the PIDs and stuff

        self.elevator_zero = False

        self.set_values()

    def set_position(self, position):
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
        #SmartDashboard.putNumber("Elevator Velocity", self.elevatorleader.getSelectedSensorVelocity(0))
        #SmartDashboard.putNumber("Elevator Current", self.elevatorleader.getOutputCurrent())
        #SmartDashboard.putNumber("Elevator Output", self.elevatorleader.getMotorOutputPercent())

    def check_for_zero(self):
        if not self.elevator_zero:
            if self.elevatorleader.isFwdLimitSwitchClosed():
                self.elevatorleader.setSelectedSensorPosition(0, 0, 0)
                self.elevator_zero = True

    def initDefaultCommand(self):
        self.setDefaultCommand(elv_zero())

    def get_position(self):
        return self.elevatorleader.getSelectedSensorPosition(0)
