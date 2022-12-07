#!/usr/bin/env python3
import time
import os
import getpass
currentUser = getpass.getuser()
lowBatteryPercentage = 10
criticalBatteryPercentage = 4
os.system('zenity --info --text="batterantix sedang berjalan di backround oleh user ' + currentUser + '" --timeout=3')
def powerFunction():
    current_stat=open("/sys/class/power_supply/BAT0/capacity","r").readline().strip()
    return current_stat
def chargeState():
    charge_state=open("/sys/class/power_supply/BAT0/status","r").readline().strip()
    return charge_state
powerStat = 100
while True:
    time.sleep(5)
    powerStat = powerFunction()
    chargeStat = chargeState()
    triggerOnce = 0
    if triggerOnce == 0:
        if int(powerStat)<=int(lowBatteryPercentage) and chargeStat == "Discharging":
            if int(powerStat)<=int(criticalBatteryPercentage):
                os.system('play -q -v 0.3 /opt/win10-lowbatt.mp3 & zenity --warning --text="Sistem akan segera dimatikan" --timeout=5')
                #os.system('poweroff')
                triggerOnce = 1
            else:
                os.system('play -q -v 0.3 /opt/win10-lowbatt.mp3 & zenity --warning --text="Baterai tersisa ' + powerStat + '%" --timeout=5')
                triggerOnce = 1
        elif int(powerStat)>=99 and chargeStat == "Full":
            os.system('play -q -v 0.3 /opt/win10-lowbatt.mp3 & zenity --warning --text="Baterai penuh" --timeout=5')
            triggerOnce = 1
