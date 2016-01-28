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
#Camera = picamera.PiCamera() 
#ResX = 800
#ResY = 600
#Camera.vflip=True
#Camera.hflip=True
#Camera.resolution = (ResX, ResY)
#Camera.framerate = 30
# Wait for the automatic gain control to settle
#time.sleep(2)
# Now fix the values
#self.Camera.shutter_speed = self.Camera.exposure_speed
#self.Camera.exposure_mode = 'off'
#g = self.Camera.awb_gains
#self.Camera.awb_mode = 'off'
#self.Camera.awb_gains = g    
panMin = 80  # Min pulse length out of 4096
panMax = 650  # Max pulse length out of 4096
tiltMin = 80  # Min pulse length out of 4096
tiltMax = 650  # Max pulse length out of 4096

panChan=0
tiltChan=1
pwm.setPWMFreq(60)
# Set frequency to 60 Hz

Imname = '/var/www/html/webcam.jpg'
pan = panMin
tilt = tiltMin
pwm.setPWM(panChan, 0, pan)
pwm.setPWM(tiltChan, 0, tilt)
time.sleep(1)
print "Drone!"
while False:
  
  char=screen.getch()
  if char==113: break
  elif char== curses.KEY_RIGHT :
    pan-=1
    pwm.setPWM(panChan, 0, pan)
  elif char== curses.KEY_LEFT : 
    pan+=1
    pwm.setPWM(panChan, 0, pan)
  elif char== curses.KEY_UP :
    tilt-=1
    pwm.setPWM(tiltChan, 0, tilt)
  elif char== curses.KEY_DOWN :
    tilt+=1
    pwm.setPWM(tiltChan, 0, tilt)
  else : pass                            

while pan<panMax:
  pan+=1
  pwm.setPWM(panChan, 0, pan)
  time.sleep(.01)
  print pan, tilt
while pan>panMin:
  pan-=1
  pwm.setPWM(panChan, 0, pan)
  time.sleep(.01)
  print pan, tilt
pan=0
pwm.setPWM(panChan, 0, pan)

while tilt<tiltMax:
  tilt+=1
  pwm.setPWM(tiltChan, 0, tilt)
  time.sleep(.01)
  print pan, tilt
while tilt>tiltMin:
  tilt-=1
  pwm.setPWM(tiltChan, 0, tilt)
  time.sleep(.01)
  print pan, tilt

tilt=0
pwm.setPWM(tiltChan, 0, tilt)

curses.endwin()  
