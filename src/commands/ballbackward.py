from wpilib.command import Command


class BallIntake(Command):

    def __init__(self):
        super().__init__("Make ball go backwards")

        self.requires(self.getRobot().ballintake)



    def initialize(self):
        print("ballbackward") + str(self))
        self.getRobot().ballintake.backward()

    def isFinished(self):
        return True
