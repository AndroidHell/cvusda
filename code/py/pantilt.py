#!/usr/bin/python
import picamera
import picamera.array
import cv2
import numpy as np
from Adafruit_PWM_Servo_Driver import PWM
import time
import sys
# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

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
i=0
Imname = '/var/www/html/webcam.jpg'
pan = int(sys.argv[1])
tilt = int(sys.argv[2])
pwm.setPWM(0, 0, pan)
pwm.setPWM(1, 0, tilt)
time.sleep(1)
Camera.capture(Imname)



