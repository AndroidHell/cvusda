import cv2
import numpy as np
import os
import csv
import time
def testwrite(img,year,doy,plot, pfx):
    oname = "../../pics/{}/{}/{}{}.JPG".format(year,doy,pfx,plot) 
    retval=cv2.imwrite(oname,img)
    print "Wrote ", oname, retval        

def testread(year,doy,plot):
    imname = "../../pics/{}/{}/{}.JPG".format(year,doy,plot) 
    img = cv2.imread(imname)
    if img==None:
        imname = "../../pics/{}/{}/{}.jpg".format(year,doy,plot)
        img = cv2.imread(imname)
    if img==None:
        imname = "../../pics/{}/{}/P{}.JPG".format(year,doy,plot)
        img = cv2.imread(imname)
    if img==None:
        imname = "../../pics/{}/{}/p{}.JPG".format(year,doy,plot)
        img = cv2.imread(imname)
    if img != None:
        print "Read ", imname
    return img

def nothing(x):
    pass

def normalize(x):
    y=(x-np.min(x))/(np.max(x)-np.min(x))*255
    return y

hn = 0
vn = 0
hT = 0
vT = 0

an = 0
Ln = 0
aT = 127
LT = 127

for year in range(2011,2013):
    treatfile='../../pics/{}/treatments{}.csv'.format(year,year)
    with open(treatfile, 'rb') as fi:
        reader = csv.reader(fi)
        for row in reader:
            plot = int(row[0])
            sector = int(row[1])
            doy = int(row[2])
            infect = int(row[3])
            water = int(row[4])
            block = int(row[5])  
            img=testread(year,doy,plot)
            if img==None:
                pass
            else:
                while np.size(img)>5000000:
                    img=cv2.pyrDown(cv2.pyrDown(img))
                hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
                h,s,v=cv2.split(hsv)
                L,a,b=cv2.split(lab)
                retval,vt = cv2.threshold(v,0,1,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
#                kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*vn+1,2*vn+1))
#                vt = cv2.morphologyEx(vt, cv2.MORPH_OPEN, kernel)
                litfrac = float(np.sum(vt>0))/float(np.size(vt))
                print litfrac, retval, np.mean(v[vt>0]), np.mean(v[vt==0])
                

                testwrite(v,year,doy,plot, "V_")
                testwrite(vt*255,year,doy,plot, "VT_")
                retval,ht = cv2.threshold(h,0,1,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
#                kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*hn+1,2*hn+1))
#                ht = cv2.morphologyEx(ht, cv2.MORPH_OPEN, kernel)
                vegfrac = float(np.sum(ht>0))/float(np.size(ht))
                print vegfrac, retval, np.mean(h[ht>0]), np.mean(h[ht==0])
                

                testwrite(h,year,doy,plot, "H_")
                testwrite(ht*255,year,doy,plot, "HT_")
                retval,Lt = cv2.threshold(L,0,1,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)
#                kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*Ln+1,2*Ln+1))
#                Lt = cv2.morphologyEx(Lt, cv2.MORPH_OPEN, kernel)
                litfrac = float(np.sum(Lt>0))/float(np.size(Lt))
                print litfrac, retval, np.mean(L[Lt>0]), np.mean(L[Lt==0])
                

                testwrite(L,year,doy,plot, "L_")
                testwrite(Lt*255,year,doy,plot, "LT_")
                retval,at = cv2.threshold(a,0,1,cv2.THRESH_TOZERO_INV+cv2.THRESH_OTSU)
#                kernel =  cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2*an+1,2*an+1))
#                at = cv2.morphologyEx(at, cv2.MORPH_OPEN, kernel)
                vegfrac = float(np.sum(at>0))/float(np.size(at))
                print vegfrac, retval, np.mean(a[at>0]), np.mean(a[at==0])
                

                testwrite(a,year,doy,plot, "A_")
                testwrite(at*255,year,doy,plot, "AT_")
