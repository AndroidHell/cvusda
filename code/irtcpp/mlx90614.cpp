#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <iostream>
#include <string.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <linux/i2c-dev.h>
 
#define MLX_ADD     0x5a
#define MLX_TEMP   0x07

using namespace std;

const char *filename = "/dev/i2c-1";
double tempfactorMLX = 0.02;

short int reverse_byte_order(short int msg){
  return ((msg<<8) & 0xFF00)|((msg>>8) & 0x00FF);
}

class MLX{
private:
  int fd;
  double temp;
  short unsigned int msg;
public:
  double readTemp(); 
  MLX(void);
  ~MLX(void);
};

MLX::MLX(void){
  if ((fd = open(filename, O_RDWR)) < 0) {        // Open port for reading and writing
    perror("Failed to open i2c port");
    //return -1;
  }

  if (ioctl(fd, I2C_SLAVE, MLX_ADD) < 0) {        // Set the port options and set the address of the device we wish to speak to
    perror("Unable to get bus access to talk to slave");
    close(fd);
    //return -1;
  }
}

double MLX::readTemp(void){
  msg = i2c_smbus_read_word_data(fd, MLX_TEMP);
  //msg = reverse_byte_order(msg); 
  temp = tempfactorMLX*double(msg);
  cout << temp << " K" << std::endl;
  return temp;
}

MLX::~MLX(void){
}
