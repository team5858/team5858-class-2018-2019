"""
Take a ball in
"""
from wpilib.command import Command
import subsystems

class SetElvPay (Command):
    """stow arm """

    def __init__(self,pay,elv):
        super().__init__("stow arm")

        self.requires(subsystems.PAYLOAD)
        self.requires(subsystems.ELEVATOR)
        self.pay_pos = pay
        self.elv_pos = elv

    def initialize(self):
        #subsystems.PAYLOAD.set_values()
        #subsystems.PAYLOAD.set_position(self.pay_pos)
        subsystems.ELEVATOR.set_values()
        subsystems.ELEVATOR.set_position(self.elv_pos)

    def execute(self):
        subsystems.ELEVATOR.publish_data()
        subsystems.PAYLOAD.publish_data()

    def isFinished(self):
        return subsystems.PAYLOAD.get_position() == self.pay_pos and subsystems.ELEVATOR.get_position() == self.elv_pos