xenserver-automation
=========

These are the scripts which will automate the daily working tasks in the hypervisor. 

inventory.py: xenserver inventory script that you can run as cron job everyday to list out the name of the vm's running under xenserver host. 
You need to keep the uuid of the xenserver hosts in the file called "xenserver-host.txt"

vm-start.py : There are situations when we have to start multiple vm's which went down during the activity in xenserver cluster. 
We can start them using their name-label. You need to copy all the vm's name and place it in the file named vm.txt. Place vm.txt file on any of the xenserver host

xentools.yml: This is the yaml script which requires ansible software to run. This script will install the xentools on the centos/Ubuntu vm in an automated fashion.
