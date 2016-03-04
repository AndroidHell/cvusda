import pantilt
import mlx90614

position=pantilt.PanTilt()
position.drone()
tmp = mlx90614.MLX()
print tmp.readObjTempK()
