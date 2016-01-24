#include <iostream>
#include <stdlib.h>
#include <bcm2835.h>

using namespace std;

class MLX{
private:
  double tempfactor;
public:
  double readTemp();
  MLX(void);
  ~MLX(void);
};

MLX::MLX(void){
  tempfactor = 0.02;

  if(!bcm2835_init()){
    cout<<"Failed bcm2835 init"<<std::endl;
    return;
  };

  bcm2835_i2c_begin();
  bcm2835_i2c_set_baudrate(25000);
  bcm2835_i2c_setSlaveAddress(0x5a);  
}

double MLX::readTemp(void){
  char buf[6];
  char reg;
  double temp=0;
  reg=7;
  bcm2835_i2c_write(&reg, 1);
  bcm2835_i2c_read_register_rs(&reg, &buf[0],3);
  temp = tempfactor * (double)(buf[0]+(buf[1]<<8));
  cout<<temp<<" K"<<std::endl;
  return temp;
}

MLX::~MLX(void){
  bcm2835_i2c_end();
  bcm2835_close();
}
