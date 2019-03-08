from ctre import ControlMode

def set_motor(motor, brake, inverted):
    motor.enableCurrentLimit(False)
    motor.configPeakOutputForward(1, 0)
    motor.configPeakOutputReverse(-1, 0)
    motor.setNeutralMode(brake)
    motor.configOpenLoopRamp(0, 0)
    motor.setInverted(inverted)
    motor.set(ControlMode.PercentOutput, 0.0)
    motor.configPeakCurrentLimit(int(60), 0)
    motor.enableCurrentLimit(True)
