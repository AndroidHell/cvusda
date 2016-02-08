from Adafruit_PWM_Servo_Driver import PWM
import time
import sys
import curses

class PanTilt(object):
    def __init__(self):
        
# Initialise the PWM device using the default address
        self.pwm = PWM(0x40)
        self.panMin = 80  # Min pulse length out of 4096
        self.panMax = 650  # Max pulse length out of 4096
        self.tiltMin = 80  # Min pulse length out of 4096
        self.tiltMax = 650  # Max pulse length out of 4096

        self.panChan=0
        self.tiltChan=1
        self.pwm.setPWMFreq(60)
        # Set frequency to 60 Hz
        self.pan = self.panMin
        self.tilt = self.tiltMin
        self.pwm.setPWM(self.panChan, 0, self.pan)
        self.pwm.setPWM(self.tiltChan, 0, self.tilt)
        time.sleep(1)
    def drone(self):
        # get the curses screen window
        self.screen = curses.initscr()
        
        # turn off input echoing
        curses.noecho()
    
        # respond to keys immediately (don't wait for enter)
        curses.cbreak()

        # map arrow keys to special values
        self.screen.keypad(True)
        print "Drone!"
        while True:
  
            self.char=self.screen.getch()
            if self.char==113: 
                curses.endwin()  
                break
            elif self.char== curses.KEY_RIGHT :
                self.pan-=1
                self.pwm.setPWM(self.panChan, 0, self.pan)
            elif self.char== curses.KEY_LEFT : 
                self.pan+=1
                self.pwm.setPWM(self.panChan, 0, self.pan)
            elif self.char== curses.KEY_UP :
                self.tilt-=1
                self.pwm.setPWM(self.tiltChan, 0, self.tilt)
            elif self.char== curses.KEY_DOWN :
                self.tilt+=1
                self.pwm.setPWM(self.tiltChan, 0, self.tilt)
            else : pass                            

test=PanTilt()
test.drone()
