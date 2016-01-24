import cv2
import numpy as np
import os
import csv

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
def labels_to_rgb_2(labels,rows,cols):
    
    R=np.uint8((labels==1)*255)
    G=np.uint8((labels==1)*255)
    B=np.uint8((labels==1)*255)
    B=B.reshape((rows,cols))
    G=G.reshape((rows,cols))
    R=R.reshape((rows,cols))
    
    segment=np.uint8(cv2.merge((B,G,R)))

    return segment

def em_2class(mat):
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
    segment=labels_to_rgb_2(result,rows,cols)
    return segment, em
    

for year in range(2012,2013):
    treatfile='../../pics/{}/treatments{}cotton.csv'.format(year,year)
    with open(treatfile, 'rb') as fi:
        reader = csv.reader(fi)
        for row in reader:
            plot = int(row[0])
            sector = int(row[1])
            doy = int(row[2])
            block = int(row[3])  
            water = int(row[4])  
            img=testread(year,doy,plot)
            if img==None:
                pass
            else:
                
                while np.size(img)>5000000:
                    img=cv2.pyrDown(cv2.pyrDown(img))
                hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
                h,s,v=cv2.split(hsv) 
                testwrite(v,year,doy,plot, "V_")
                testwrite(h,year,doy,plot, "H_")
                hem,emh=em_2class(h)
                testwrite(hem,year,doy,plot, "HEM_")
                vem,emv=em_2class(v)
                testwrite(vem,year,doy,plot, "VEM_")
