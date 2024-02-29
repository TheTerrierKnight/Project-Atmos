# Inport All needed Stuff
import turtle
import random
import time
import os
# Start Up CMD Line (DO NOT TOUCH)
GlobalPath = [36/34/67/44/22/33/44/55] # Does Nothing yet :(
GlobalPrefix = "AtmosProton.py" # Does nothing yet :(
AdminPrefix = "!"
print("Starting Peloading")
time.sleep(1)
print("Preloading Finished! Setting Up Configs and Starting Atmos-CMD")

# GLOBAL CONFIGS (Use 0 or 1)
UseGlobalPrefix = 0
UseGlobalPath = 0
RunCMD = 1 # Runs the Code
NoticeTest = 1 # Test for AEN Manager


# Alert/Error/Notice Manager (AEN Manager)

#Notices
if NoticeTest == 1:
 print("Notice: NoticeTest is Enabled.")

#Errors

#Alerts
if RunCMD != 1:
 print("Error: RunCMD is not 1, Please Check RunCMD.")

# End of AEN Manager








# MAIN CODE

# Atmos-CMD (Proton) 

while RunCMD == True:
   command = input("Atmos-CMD: ")
   if command == (AdminPrefix + "RunTest"):
    print("Running...")
    time.sleep(1)
    print("Wohoo! The Prefix Works!")
   if command == ("help"):
    print("version-1,version-2,forward,backward,left,right,color select,exit,purge")
   if command == ("purge"):
    os.system("cls")
   if command == "version-1":
    print("You are Running AtmosProtonCMD-V1")
   if command == "version-2":
    print("You are Running Atmos/Proton/V1.0.2.3")
   if command == "forward":
    distance = float(input("Provide Distance of Movement: "))
    turtle.forward(distance)
   if command == "backward":
    distance = float(input("Provide Distance of Movement: "))
    turtle.backward(distance)
   if command == "left":
    distance = float(input("Provide Distance of Movement: "))
    turtle.left(distance)
   if command == "right":
    distance = float(input("Provide Distance of Movement: "))
    turtle.right(distance)
   if command == "color select":
    color = str(input("Provide Color: "))
    turtle.color(color)
   if command == "exit":
    turtle.done()
   
    