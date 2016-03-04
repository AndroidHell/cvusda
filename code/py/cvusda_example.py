import agcv
import pantilt
import mlx90614

position=pantilt.PanTilt()
#Move camera with arrow keys - "q" to quit
position.drone()
test = agcv.CV()
#Otsu segmentation
test.OtsuHV()
#EM segmentation
test.emHV()
#read the Melexis IR sensor
tmp = mlx90614.MLX()
print tmp.readObjTempK()
