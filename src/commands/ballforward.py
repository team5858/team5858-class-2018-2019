from wpilib.command import Command

class BallIntake(Command):

    def __init__(self):
        super().__init__("Make ball go forwards")


        self.requires(self.getRobot().ballintake)



    def initialize(self):
        print("ballforward") +str(self))
        self.getRobot().ballintake.forward()


    def isFinished(self):
            return True

