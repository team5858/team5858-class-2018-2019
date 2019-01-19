import wpilib
from wpilib.command.subsystem import Subsystem
from ctre.victorspx import VictorSPX
import ctre.victorspx

#pwm = 6
import wpilib
from wpilib.command.subsystem import Subsystem

class Vacuum(Subsystem):


    def __init__(self):

        super().__init__("Vacuum")
        self.vacmotor = VictorSPX (6)



    def set_motor (self,on_off):
        if on_off:
            self.vacmotor.
        else:
            self.vacmotor.stopMotor()

