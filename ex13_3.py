#this file is an attempt to combine input from the commandline With
#input from within the script
from sys import argv
script, first, second =argv
myname= input("What is your name? ")
print(f"How are you {myname}?")
print(f"{first} and {second} are waiting in the lobby")
