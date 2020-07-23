#!/bin/python

import sys
import subprocess
with open("vm.txt", "r") as instance:
  for line in instance:
    cmd = 'xe vm-list params=power-state uuid='+line
#  cmd = 'xe vm-start name-label='+vm
    power = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    state = power.communicate()[0]
    powerstate = (state[23:30])
    if powerstate == "halted\n" :
           vm = 'xe vm-start uuid='+line
           subprocess.Popen(vm,shell=True)
           print ('started the vm:'+line)
    else:
           print ('vm is running')
#    print (powerstate)
#  instance.close()
