#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <linux/i2c-dev.h>
#include "./tmp007.h"
#include "./mlx90614.h"

int main(void){

  MLX test;
  
  test.readTemp();

  TMP test2;

  test2.objTemp();

  return 0;

};

