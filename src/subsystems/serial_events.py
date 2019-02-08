from wpilib.command.subsystem import Subsystem
from wpilib.serialport import SerialPort

# http://www.ni.com/pdf/manuals/374474a.pdf

'''
Pinout for the MXP Port

    1 2
    3 4
    5 6
    7 8
    9 10 UART-RX
   11 12 DGND      <-- Connect ground
   13 14 UART-TX   <-- Spew FROM the robot
   15 16
   17 18
   19 20
   21 22
   23 24
   25 26
   27 28
   29 30
   31 32
   33 34
'''


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
