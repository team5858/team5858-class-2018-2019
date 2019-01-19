import wpilib
from wpilib.command.subsystem import Subsystem

from wpilib.victorsp import VictorSP

#pwm = 6
import wpilib
from wpilib.command.subsystem import Subsystem

class Vacuum(Subsystem):


    def __init__(self):

        super().__init__("Vacuum")
        self.vacmotor = VictorSP(6)



    def set_motor (self,on_off):
        if on_off:
            self.vacmotor.setSpeed(0.5)
        else:
            self.vacmotor.stopMotor()

