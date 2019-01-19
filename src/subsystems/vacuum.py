

#pwm = 6
import wpilib
from wpilib.command.subsystem import Subsystem

class Vacuum(Subsystem):


    def __init__(self):

        super().__init__("Vacuum")




    def set_motor (self,on_off):
        pass

