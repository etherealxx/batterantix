#!/usr/bin/env python3
import time
import os
import getpass

criticalBatteryPercentage = 4

currentUser = getpass.getuser()
os.system('echo batterantixcrit sedang berjalan di backround oleh user ' + currentUser)
def powerFunction():
    current_stat=open("/sys/class/power_supply/BAT0/capacity","r").readline().strip()
    return current_stat
def chargeState():
    charge_state=open("/sys/class/power_supply/BAT0/status","r").readline().strip()
    return charge_state
powerStat = 100
while True:
    time.sleep(10)
    powerStat = powerFunction()
    chargeStat = chargeState()
    triggerOnce = 0
    if triggerOnce == 0:
        if int(powerStat)<=int(criticalBatteryPercentage) and chargeStat == "Discharging":
            os.system('poweroff')
            triggerOnce = 1
