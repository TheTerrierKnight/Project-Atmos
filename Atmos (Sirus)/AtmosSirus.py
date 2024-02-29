# Inport needed Libraries
import os
import time
import random as rand

# GLOBAL CONFIGS/SIMULATION CONFIGS

# AEN 
BetaWarningAacknowledge = 1

# HeatIndex
HeatVector = 24 # HeatTemp*HeatVector
AirPrefix = 1 # Air Pressure Complex
HeatTemp = 32 # Temp of Air Currently

 
# BottleTemp V2
BottleTargetTemp = 56 # Temp you Need
AvegTemp = 35 # Temp Right now
TempBottle = 36 # Bottle Temp


#AEN Manager

#Alerts

#Errors

#Notices
if BetaWarningAacknowledge != 1:
 print("Notice: Scout is in Beta, Please report issues that ouccur")
else:
 print("You Have a Hidden Notice")

#Fire Up The Simulation
print("Beginning Preloading... This Can Take A Minute")
time.sleep(rand.randint(27,63))
print("Preload Finished! Loading SimulationManager...")
time.sleep(rand.randint(3,7))
print("Loading Finished! Starting Atmos-CMD")
time.sleep(1.5)
print("------------------------------------------------------------------")
time.sleep(1.5)
print("------------------------------------------------------------------")
time.sleep(1.5)
print("------------------------------------------------------------------")

while True:
  command = input("Atmos-SIM/CMD: ")
  if command == ("help"):
   print("version-1,verson-2,start-simulaton-type-[SIM-NAME]")
  if command == ("verson-1"):
   print("You are Running AtmosSirusCMD-V0.2")
  if command == ("verson-2"):
   print("You are Running Atmos/Sirus/V0.2.2")
  if command == ("start-simulaton-type-HeatIndex"):
   print("Doing Amazing math. Stand By...")
   time.sleep(rand.randint(4,7))
   print("Your Heat Index: ")
   print((HeatVector*HeatTemp)*AirPrefix)
  if command == ("start-simulaton-type-BottleTemp-V2"):
   print("Trying to Find the Target Temp Diffrence...")
   time.sleep(rand.randint(3,6))
   print("Your Target Temp is off by: ")
   print((AvegTemp+TempBottle)-BottleTargetTemp)