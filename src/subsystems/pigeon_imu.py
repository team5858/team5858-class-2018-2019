import ctre.pigeonimu

from wpilib.command.subsystem import Subsystem

PIGEON_CAN_ID = 14

class Pigeon(Subsystem):
    """
    For the pigeon IMU
    """

    def __init__(self):
        super().__init__("PigeonIMU")
        self._pigeon = ctre.pigeonimu.PigeonIMU(PIGEON_CAN_ID)

    def get_position(self):
        pass

