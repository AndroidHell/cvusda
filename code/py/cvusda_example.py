import agcv
import pantilt
import mlx90614

position=pantilt.PanTilt()
position.drone()
test = agcv.CV()
test.OtsuHV
tmp = mlx90614.MLX()
print tmp.readObjTempK()
