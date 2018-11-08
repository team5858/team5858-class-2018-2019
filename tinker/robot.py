#!/usr/bin/env python3

import wpilib
import wpilib.buttons

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        # This function is called upon program startup and
        # should be used for any initialization code.
        
        self.stick = wpilib.Joystick(1)
        self.timer = wpilib.Timer()
        
        self.led1 = wpilib.DigitalOutput(0)  # LED hooked up to Digital Output 0
        self.switch = wpilib.DigitalInput(1) # Switch hooked up to Digital Input 1
        self.led2 = wpilib.DigitalOutput(2)  # LED hooked up to Digital Output 2
        
        self.servo = wpilib.Servo(0) # PWM channel 0        
        
        self.a_button = wpilib.buttons.JoystickButton(self.stick,1)

    def autonomousInit(self):
        # This function is run once each time the robot enters autonomous mode.
        print("In here. Where does this text go?")
        self.servo.set(0.5) # From 0.0 to 1.0
        
    def autonomousPeriodic(self):
        #This function is called periodically during autonomous.
        pass     

    def teleopPeriodic(self):
        #This function is called periodically during operator control.
        
        if self.a_button.get():
            self.led1.set(True)
        else:
            self.led1.set(False)
            
        if self.switch.get():
            self.led2.set(True)
        else:
            self.led2.set(False)
            
        # How about this instead:
        # self.led2.set(self.switch.get())

if __name__ == "__main__":
    wpilib.run(MyRobot)