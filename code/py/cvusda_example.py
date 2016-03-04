import agcv
import pantilt
import mlx90614

#position=pantilt.PanTilt()
#position.drone()
test = agcv.CV()
test.OtsuHV()
test.emHV()

tmp = mlx90614.MLX()
print tmp.readObjTempK()
