import wpilib
from wpilib.command.subsystem import Subsystem

class LimitSwitch(wpilib.IterativeRobot):

    def robotInit(self):
        self.forwardLimitSwitch = wpilib.DigitalInput(1)
        self.reverseLimitSwitch = wpilib.DigitalInput(2)
        self.joystick1 = wpilib.Joystick(1)
        self.motor = wpilib.Talon(1)

    def teleopPeriodic(self):
        output = self.Joystick1.getY()
        if self.forwardLimitSwitch.get():
            output = min(0, output)
        elif self.reverseLimitSwitch.get():
            output = max(0, output)

        motor.set(output)