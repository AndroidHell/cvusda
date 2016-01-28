#!/usr/bin/python
import picamera
import picamera.array
import cv2
import numpy as np
from Adafruit_PWM_Servo_Driver import PWM
import time
import sys
import curses

# get the curses screen window
screen = curses.initscr()

# turn off input echoing
curses.noecho()

# respond to keys immediately (don't wait for enter)
curses.cbreak()

# map arrow keys to special values
screen.keypad(True)
# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)
Camera = picamera.PiCamera() 
ResX = 800
ResY = 600
Camera.vflip=True
Camera.hflip=True
Camera.resolution = (ResX, ResY)
Camera.framerate = 30
# Wait for the automatic gain control to settle
time.sleep(2)
# Now fix the values
#self.Camera.shutter_speed = self.Camera.exposure_speed
#self.Camera.exposure_mode = 'off'
#g = self.Camera.awb_gains
#self.Camera.awb_mode = 'off'
#self.Camera.awb_gains = g    
servoMin = 50  # Min pulse length out of 4096
servoMax = 450  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)
# Set frequency to 60 Hz

Imname = '/var/www/html/webcam.jpg'
pan = int(sys.argv[1])
tilt = int(sys.argv[2])
setServoPulse(0, pan)
setServoPulse(1, tilt)
time.sleep(1)
print "Drone!"
while True:
  time.sleep(1)
  char=screen.getch()
  if char==113: break
  elif char== curses.KEY_RIGHT :
    pan+=1
    setServoPulse(0, pan)
  elif char== curses.KEY_LEFT : 
    pan-=1
    setServoPulse(0, pan)
  elif char== curses.KEY_UP :
    tilt+=1
    setServoPulse(1, tilt)
  elif char== curses.KEY_DOWN :
    tilt-=1
    setServoPulse(1, tilt)
  else : pass
  Camera.capture(Imname)
                                         


