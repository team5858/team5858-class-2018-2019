"""
Command group to blink the red LED 4 times
"""

from commands.set_red_led import SetRedLED
from wpilib.command.commandgroup import CommandGroup
from wpilib.command.waitcommand import WaitCommand

class AutonomousProgram(CommandGroup):
    """
    A simple sequence that blinks the red led 4 times.
    """

    def __init__(self):
        super().__init__("Autonomous Program")

        print("HERE IN AUTONOMOUS PROGRAM")

        self.addSequential(SetRedLED(True))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(SetRedLED(False))
        self.addSequential(WaitCommand(timeout=1))

        self.addSequential(SetRedLED(True))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(SetRedLED(False))
        self.addSequential(WaitCommand(timeout=1))

        self.addSequential(SetRedLED(True))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(SetRedLED(False))
        self.addSequential(WaitCommand(timeout=1))

        self.addSequential(SetRedLED(True))
        self.addSequential(WaitCommand(timeout=1))
        self.addSequential(SetRedLED(False))
        self.addSequential(WaitCommand(timeout=1))
