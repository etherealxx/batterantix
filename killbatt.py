#!/usr/bin/env python3
import os, signal

try:
         
    # iterating through each instance of the process
    for line in os.popen("ps ax | grep batterantix | grep -v grep"):
        fields = line.split()
             
        # extracting Process ID from the output
        pid = fields[0]
             
        # terminating process
        os.kill(int(pid), signal.SIGKILL)
    print("Batterantix Successfully terminated")
         
except:
    print("Batterantix process not found/not enough permission")
