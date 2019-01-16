from wpilib.command import Command

class GreenLEDOn(Command):
    """
    This command will set the RED LEDs state.
    """

    def __init__(self,state):
        super().__init__("Set the state of the green LED")

        self.requires(self.getRobot().leds)

        self._state = state

    def initialize(self):
        """Called just before this Command runs the first time"""
        print("GreenLEDOn init: "+str(self._state))
        self.getRobot().leds.set_green(self._state)

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return True
