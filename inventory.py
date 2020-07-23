xenserver inventory script that runs everyday to list out the name of the vm's running under xenserver host. 
You need to keep the uuid of the xenserver in the file called "xenserver-host.txt"


#!/bin/python

import sys
import subprocess
with open("xenserver-host.txt", "r") as host:
  for line in host:
     cmd = 'xe vm-list params=name-label resident-on='+line
     list_vm = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
     state = list_vm.communicate()[0]
     print "VM running under xenserver host with the uuid: "+line+"\n", state
