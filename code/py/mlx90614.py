import smbus
#import os

MLX_I2CADDR = 0x5A
MLX_TEMP = 0x07
BUSNUM = 1
class MLX(object):
    def __init__(self):
#        os.system("echo -n 1> /sys/module/i2c_bcm2708/parameters/combined")
        # Create I2C device.
        self._device = smbus.SMBus(BUSNUM)
    # read Obj Temp in K
    def readObjTempK(self):
        raw = self._device.read_word_data(MLX_I2CADDR, MLX_TEMP)
        Tobj = raw
        Tobj *= 0.02 # convert to celsius
        return Tobj
