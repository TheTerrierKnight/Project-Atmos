# Start Up CMD Line (DO NOT TOUCH)
GlobalPath = [36/34/67/44/22/33/44/55] # Does Nothing yet :(
GlobalPrefix = "AtmosProton.py" # Does nothing yet :(
AdminPrefix = "!"
print("Preloading Finished! Setting Up Configs and Starting Atmos-CMD")
# Inport All needed Stuff
import turtle
import random
import time

# GLOBAL CONFIGS
UseGlobalPrefix = 0
UseGlobalPath = 0
RunCMD = 1 # Runs the Code
NoticeTest = 1


# Alert/Error/Notice Manager
 #Notices
if NoticeTest == 1:
 print("Notice Test is Enabled.")


# Atmos-CMD (Proton) 

while RunCMD == True:
   command = input("Enter a Command: ")
   if command == (AdminPrefix + "RunTest"):
    print("Running...")
    time.sleep(1)
    print("Wohoo! The Prefix Works!")
   if command == ("Help"):
    print("version-1,version-2,forward,backward,left,right,color select,exit")
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
   
    