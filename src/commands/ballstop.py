from wpilib.command import Command


class BallIntake(Command):

    def __init__(self):
        super().__init__("Make ball stop")

        self.requires(self.getRobot().ballintake)



    def initialize(self):
        print("ballstop") + str (self))
        self.getRobot().ballintake.stop()

    def isFinished(self):
        return True
