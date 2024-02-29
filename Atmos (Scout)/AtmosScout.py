# Inport Needed Stuff
import os
import time
GlobalPath = [36/34/67/44/22/33/44/55]
SpaceDeco = " "
# Global Configs
PreloadSafety = 1
BetaWarningAacknowledge = 1
# Start up Scout
if PreloadSafety == 1:
 print("Starting Preloading...")
 time.sleep(3)
 print("Preload Finished! Loading OS/TIME")
 time.sleep(2)
 print("Loaded! Starting Atmos-CMD")
else:
 print("Starting Atmos-CMD")

#AEN Manager

#Alerts

#Errors

#Notices
if PreloadSafety != 1:
 print("Notice: Preloading is Disabled! Scout will lag sometimes if this is Disabled!")
if BetaWarningAacknowledge != 1:
 print("Notice: Scout is in Beta, Please report issues that ouccur")
else:
 print("You Have a Hidden Notice")
 





 

# Atmos-CMD (Scout)


while True:
  command = input("Atmos-CMD: ")
  if command == ("help"):
   print("merge,purge,verson-1,verson-2,mult,split,math-circle,find-perimeter,calculate-datapoint-RMS,temp-F-C,temp-C-F,money")
  if command == ("version-1"):
   print("You are Running AtmosScoutCMD-V0.5")
  if command == ("version-2"):
   print("You are Running Atmos/Scout/V0.5.1")
  if command == ("purge"):
   os.system("cls")
  if command == ("merge"):
   Prompt1 = int(input("Provide 1st Prompt: "))
   Prompt2 = int(input("Provide 2nd Prompt: "))
   print(Prompt1+SpaceDeco+Prompt2)
  if command == ("mult"):
   Mult1 = int(input("Provide 1st Var: "))
   Mult2 = int(input("Provide 2nd Var: "))
   print(Mult1*Mult2)
  if command == ("split"):
   Split1 = int(input("Provide 1st Var: "))
   Split2 = int(input("Provide 2nd Var: "))
   print(Split1/Split2)
  if command == ("math-circle"):
   NumCircle1 = int(input("Provide Raidus: "))
   print(NumCircle1*3.14*2)
  if command == ("find-perimeter"):
   SideGroupSquare1 = int(input("Provide 1st Side Group: "))
   SideGroupSquare2 = int(input("Provide 2nd Side Group: "))
   print(SideGroupSquare1+SideGroupSquare1+SideGroupSquare2+SideGroupSquare2)
  if command == ("calculate-datapoint-RMS"):
   Datapoint1 = int(input("Provide 1st Datapoint: "))
   Datapoint2 = int(input("Provide 2nd Datapoint: "))
   print("Range: ")
   print((Datapoint1-Datapoint2))
   print("Mean: ")
   print(((Datapoint1+Datapoint2)/2))
   print("Sum: ")
   print((Datapoint2+Datapoint1))
  if command == ("temp-F-C"):
   Temp1 = int(input("Provide Temperature in F: "))
   print(((Temp1-32)*5)/9)
  if command == ("temp-C-F"):
   Temp2 = int(input("Provide Temperature in C: "))
   print(((Temp2*9)/5)+32)
  if command == ("money"):
   Money1 = int(input("Provide your Income: "))
   Money2 = int(input("Provide your Tax Rate (DONT Use a % after the number): "))
   print("Your Total Income after removing Taxes: ")
   print((Money1-Money2))