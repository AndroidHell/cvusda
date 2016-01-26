#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <linux/i2c-dev.h>
//#include "./mlx90614.h"
#include "./tmp007.h"
int main(void){

  TMP test;
  
  test.objTemp();


  return 0;

};

