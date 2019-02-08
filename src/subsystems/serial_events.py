from wpilib.command.subsystem import Subsystem
from wpilib.serialport import SerialPort


class SerialEvent(Subsystem):
    """
    Spewing events over serial port
    """

    def __init__(self):
        super().__init__("Serial")
        self._serial_port = SerialPort(115200, SerialPort.Port.kMXP)

    def fire_event(self, event):
        """Send the event string over the serial port"""
        self._serial_port.writeString('[' + event + ']\r')
