import picamera
import picamera.array
import cv2
import numpy as np
import time

class CV:
    def __init__(self):
        self.Iname = '/var/www/webcam.jpg'
        self.Oname = '/var/www/post.jpg'
        self.ResX = 800
        self.ResY = 600
        self.Camera = picamera.PiCamera()
        self.Camera.vflip=True
        self.Camera.hflip=True
        self.Camera.resolution = (self.ResX, self.ResY)
        self.Camera.framerate = 30
        # Wait for the automatic gain control to settle
        time.sleep(2)
        # Now fix the values
        #self.Camera.shutter_speed = self.Camera.exposure_speed
        #self.Camera.exposure_mode = 'off'
        #g = self.Camera.awb_gains
        #self.Camera.awb_mode = 'off'
        #self.Camera.awb_gains = g

    def OtsuHV(self):
        with picamera.array.PiRGBArray(self.Camera) as stream:
            self.Camera.capture(stream, format='bgr')
            # At this point the image is available as stream.array
            img = stream.array
            cv2.imwrite(self.Iname,img)
            print "Processing..."
            while np.size(img)>5000000:
                img=cv2.pyrDown(cv2.pyrDown(img))
            hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
            h,s,v=cv2.split(hsv)
            retval,vt = cv2.threshold(v,0,1,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
            litfrac = float(np.sum(vt>0))/float(np.size(vt))
            retval,ht = cv2.threshold(h,0,1,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
            vegfrac = float(np.sum(ht>0))/float(np.size(ht))
            vegmean = np.mean(h[ht>0])
            print vegfrac, retval, np.mean(h[ht==0])
            cv2.imwrite(self.Oname,ht)
            return litfrac, vegfrac, vegmean 
    
test = CV()
test.OtsuHV()
