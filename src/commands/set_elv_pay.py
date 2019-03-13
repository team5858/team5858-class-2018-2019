"""
Take a ball in
"""
from wpilib.command import Command
import subsystems
from wpilib import Preferences

class SetElvPay (Command):
    """stow arm """

    def __init__(self,elv,pay):
        super().__init__("stow arm")

        self.prefs = Preferences.getInstance()

        self.requires(subsystems.PAYLOAD)
        self.requires(subsystems.ELEVATOR)
        self.pay_pos = pay
        self.elv_pos = elv

    def initialize(self):
       # self.pay_pos = self.prefs.getFloat("Elbow Position", 0)
        subsystems.PAYLOAD.set_values()
        subsystems.PAYLOAD.set_position(self.pay_pos)
       # print("George")

        #self.elv_pos = self.prefs.getFloat("Elevator Position", 0)
        subsystems.ELEVATOR.set_values()
        subsystems.ELEVATOR.set_position(self.elv_pos)

    def execute(self):
        subsystems.ELEVATOR.publish_data()
        subsystems.PAYLOAD.publish_data()

    def isFinished(self):
        return True
