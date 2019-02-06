import wpilib
from wpilib.command.subsystem import Subsystem


class Payload(Subsystem):
    """
    For both Hatches and Balls
    """

    def __init__(self):
        super().__init__("Payload")
        # TODO Two motors ... one leader, one follower
        # TODO Two limit switches on the follower

    def wheels_in(self):
        # TODO Spin motors to bring ball in
        pass

    def wheels_out(self):
        # TODO Spin motors to push ball out
        pass

    def wheels_stop(self):
        # TODO Stop motors
        pass

    def hatch_punch_out(self):
        # TODO send air to piston
        pass

    def hatch_punch_in(self):
        # TODO turn off air to piston
        pass
