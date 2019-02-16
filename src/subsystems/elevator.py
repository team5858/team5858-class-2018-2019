from ctre import ControlMode
from ctre import FeedbackDevice
from ctre import TalonSRX
from wpilib import Preferences
from wpilib import SmartDashboard
import wpilib
from wpilib.command.subsystem import Subsystem

CAN_ELEVATOR_LEADER = 1
CAN_ELEVATOR_FOLLOWER = 6

class Elevator(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):

        super().__init__("Elevator")

        # Initializes the elevator Talon, put it as one for now
        self.elevatorleader = TalonSRX(CAN_ELEVATOR_LEADER)
        self.elevatorleader.configSelectedFeedbackSensor(FeedbackDevice.CTRE_MagEncoder_Relative, 0, 0)
        self.elevatorleader.setSelectedSensorPosition(0, 0, 0)
        # Gives the elevator its initial setpoint, may not be 0 on the real
        # robot
        #self.elevator.set(ControlMode.MotionMagic, 0)
        # self.elevator.configSelectedFeedbackSensor(
        #    FeedbackDevice.CTRE_MagEncoder_Relative)  # Sets the sensor
        # self.elevator.config_kF(0, 0.2, 0)  # F value is based on max velocity
        # Tells the Talon which slot of the PID we are using, since we;re onliy
        # using one we'll start with 0
        #self.elevator.selectProfileSlot(0, 0)

        # The preference table is used to get values to the code while the
        # robot is running, useful
        #self.prefs = Preferences.getInstance()
        # for tuning the PIDs and stuff

    def elevator_up_down(self, position):
        # self.elevator.set(ControlMode.MotionMagic, position) # Will wet the elevator to whatver setpoint is input # commneted so we can run from
        # the preference table
        self.elevatorleader.set(ControlMode.MotionMagic, self.prefs.getFloat(
            "Elevator Position", 0))  # Will set the setpoint to whatever it is set
        # in the preference table so we can tune it

    def setPID(self):
        # This will set the PIDs, velocity, and acceleration, values from the
        # preference table so we can tune them easily
        self.elevatorleader.config_kI(0, self.prefs.getFloat("Elevator I", 0), 0)
        self.elevatorleader.config_kD(0, self.prefs.getFloat("Elevator D", 0), 0)
        self.elevatorleader.configMotionCruiseVelocity(
            self.prefs.getInt("Elevator Velocity", 0))
        self.elevatorleader.config_kP(0, self.prefs.getFloat("Elevator P", 0), 0)
        self.elevatorleader.configMotionAcceleration(
            self.prefs.getInt("Elevator Acceleration", 0))

    def publishData(self):
        # This will print the position and velocity to the smartDashboard
        # SmartDashboard.putNumber(
        #    "Elevator Position", self.elevator.getSelectedSensorPosition())
        # SmartDashboard.putNumber(
        #    "Elevator Velocity", self.elevator.getSelectedSensorVelocity())
        pass

    def get_position(self):
        return self.elevatorleader.getSelectedSensorPosition(0)




