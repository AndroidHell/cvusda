#!/bin/bash
i=0
for i in {0..255}
do
   ssh pi@10.42.1.$i
   echo pi@10.42.1.$i
done
