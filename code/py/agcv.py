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
            self.Oname = '/var/www/html/postOtsu.jpg'
            cv2.imwrite(self.Oname,ht)
            print litfrac, vegfrac, vegmean 
            return litfrac, vegfrac, vegmean 

    def em_2class(self,mat):
        rows, cols = np.shape(mat)
        means=[0, 0]
        test = mat.reshape((np.size(mat),1))
        em = cv2.EM(2,cv2.EM_COV_MAT_DIAGONAL)
        ret, ll, result, probs = em.train(test)
        rr=result.reshape((np.shape(mat)))
        means[0]=np.mean(mat[rr==0])
        means[1]=np.mean(mat[rr==1])
        if means[0]>means[1]:
            dum=result.copy()
            result[dum==1]=0
            result[dum==0]=1
        #ensures class 1 is veg or lit
        return result.reshape(rows,cols)

    def emHV(self):
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
            hem=self.em_2class(h)
            vem=self.em_2class(h)
            litfrac = float(np.sum(vem>0.0))/float(np.size(vem))
            vegfrac = float(np.sum(hem>0.0))/float(np.size(hem))
            vegmean = np.mean(h[hem>0])
            self.Oname = '/var/www/html/postEM.jpg'
            cv2.imwrite(self.Oname,hem)
            print  litfrac, vegfrac, vegmean 
            return litfrac, vegfrac, vegmean 
    
