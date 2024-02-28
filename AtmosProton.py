# Start Up CMD Line
 # nothing here yet :(


# Inport All needed Stuff
import turtle
import random
import time

# Atmos-CMD (Proton) 

while True:
   command = input("Enter a Command: ")
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