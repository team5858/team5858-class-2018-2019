from wpilib.command import Command

class SetRedLED(Command):
    """
    This command will set the RED LEDs state.
    """

    def __init__(self,state):
        super().__init__("Set the state of the red LED")

        self.requires(self.getRobot().leds)

        self._state = state

    def initialize(self):
        """Called just before this Command runs the first time"""
        print("SetRedLED init: "+str(self._state))
        self.getRobot().leds.set_red(self._state)

    #def execute(self):
    #    """Called repeatedly when this Command is scheduled to run"""
    #    pass

    def isFinished(self):
        """Make this return true when this Command no longer needs to run execute()"""
        return True

    #def end(self):
    #    """Called once after isFinished returns true"""
    #    return True

    #def interrupted(self):
    #    """Called when another command which requires one or more of the same
    #    subsystems is scheduled to run"""
    #    self.end()
