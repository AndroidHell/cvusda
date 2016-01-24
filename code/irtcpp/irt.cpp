#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/ml/ml.hpp>
#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <time.h>
#include <bcm2835.h>

using namespace cv;
using namespace std;

ofstream outfile;
char imname[30];
char outname[30];
int imnum = 0;
int imnummax = 10;
Mat image, h;
double tempfactor = 0.02;
double temp = 0;
char numstr[10];

int irtread() {

  char buf[6];
  char reg;
  reg=7;
  bcm2835_i2c_write(&reg, 1);
  bcm2835_i2c_read_register_rs(&reg, &buf[0],3);
  temp = tempfactor * (double)(buf[0]+(buf[1]<<8));
   
  return 0;
}


int sample(){

    irtread();

    cout << " " << temp << std::endl;

    return 0;
}

int main( int argc, char** argv ){

  if(!bcm2835_init()){
    cout<<"Failed bcm2835 init"<<std::endl;
    return -1;
  };

  bcm2835_i2c_begin();
  bcm2835_i2c_set_baudrate(25000);
  bcm2835_i2c_setSlaveAddress(0x5a);  
  
  sample();

  bcm2835_i2c_end();
  bcm2835_close();

  return 0;

}
