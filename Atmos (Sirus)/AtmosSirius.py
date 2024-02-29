# Inport needed Libraries
import os
import time
import random as rand
CMD = ("Path.Main.SIM/CMD") # DO NOT TOUCH

# GLOBAL CONFIGS/SIMULATION CONFIGS

# AEN 
BetaWarningAacknowledge = 1

# HeatIndex
HeatVector = 3.2 # HeatTemp*HeatVector
AirPrefix = 1 # Air Pressure Complex
HeatTemp = 32 # Temp of Air Currently

 
# BottleTemp V2
BottleTargetTemp = 56 # Temp you Need
AvegTemp = 35 # Temp Right now
TempBottle = 36 # Bottle Temp


# C-CAD V1.3
StructureVerticalHeight = 36 # Height
WindForceStructure = 23.4 # How much wind is affecting the Structure
IntegrityLossExponential = 2 # How much is the StructureIntegrity Reduced By


# BreakneckV2
RamSpeed = 2500 # Ram Speed
RamStorage = 3.4 # Maxium Storage for your RAM
RwPerMinute = 56 # Read/Write Per Minute

# MaxMinV3
MaxiumOverflow = 600 # Max
MinimumOverflow = 300 # Min

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////







#AEN Manager

#Alerts

#Errors

#Notices
if BetaWarningAacknowledge != 1:
 print("Notice: Sirius is in Beta, Please report issues that ouccur")
 print("Notice: Sirius May Provide Inaccurate Data. Please be careful when using Sirus")
else:
 print("You Have 2 Hidden Notices")


# This Setting is for Experenced Devs, Please be careful with this.
PreloadX = 27
PreloadY = 63
# Defaults = 27,63


#Fire Up The Simulation
print("Beginning Preloading... This Can Take A Minute")
time.sleep(rand.randint(PreloadX,PreloadY))
print("Preload Finished! Loading SimulationManager...")
time.sleep(rand.randint(3,7))
print("Loading Finished! Starting Atmos-CMD")
time.sleep(3)
os.system("cls")
print("------------------------------------------------------------------")
time.sleep(1.5)
print("------------------------------------------------------------------")
time.sleep(1.5)
print("------------------------------------------------------------------")


 
 
# ////////////////////////////////////////////////////////////////////////////////////////////////////////






while CMD == ("Path.Main.SIM/CMD"):
  command = input("Atmos-SIM/CMD: ")
  if command == ("help"):
   print("version-1,verson-2,purge,start-simulation-type-[SIM-NAME]")
  if command == ("version-1"):
   print("You are Running AtmosSiriusCMD-V0.2")
  if command == ("version-2"):
   print("You are Running Atmos/Sirius/V0.2.4")
  if command == ("start-simulation-type-HeatIndex"):
   print("Starting Simulation. Please wait while we process the data.")
   time.sleep(rand.randint(4,7))
   print("Your Heat Index: ")
   print((HeatVector*HeatTemp)*AirPrefix)
  if command == ("start-simulation-type-BottleTemp-V2"):
   print("Starting Simulation. Please wait while we process the data.")
   time.sleep(rand.randint(3,6))
   print("Your Target Temp is off by: ")
   print((AvegTemp+TempBottle)-BottleTargetTemp)
  if command == ("purge"):
   os.system("cls")
   time.sleep(1.5)
   print("------------------------------------------------------------------")
   time.sleep(1.5)
   print("------------------------------------------------------------------")
   time.sleep(1.5)
   print("------------------------------------------------------------------")
  if command == ("start-simulation-type-C-CAD_V1.3"):
   print("Starting Simulation. Please wait while we process the data.")
   time.sleep(rand.randint(3,6))
   print("Your Structure will Degrade Around this Pressure Force (PSI): ")
   print((StructureVerticalHeight+WindForceStructure)//IntegrityLossExponential)
  if command == ("start-simulation-type-BreakneckV2"):
   print("Starting Simulation. Please wait while we process the data.")
   time.sleep(rand.randint(3,6))
   print("Your Ram Has the Following I/O Specs: ")
   print((RamSpeed-RwPerMinute)*RamStorage)
  if command == ("start-simulation-type-MaxMinV3"):
   print("Starting Simulation. Please wait while we process the data.")
   time.sleep(rand.randint(3,6))
   print("You Max/Min MoE is: ")
   print(MaxiumOverflow-MinimumOverflow)
else:
 print("Critical Error 500: Engine Crash/Invalid Path")