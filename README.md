xenserver
=========

These are the scripts which will automate the daily working tasks in the hypervisor. 


xenserver inventory script that runs everyday to list out the name of the vm's running under xenserver host. 
You need to keep the uuid of the xenserver in the file called "xenserver-host.txt"

There are situations when we have to start multiple vm's which went down during the activity in xenserver cluster. 
We can start them using their name-label in the excel sheet. 

You need to copy all the vm's name from the excel sheet and place it in the file named vm.txt. Place vm.txt file on any of the xenserver host
