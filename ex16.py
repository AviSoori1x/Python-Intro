#import argument value from the library sys
from sys import argv
#Take whatever is in argv, unpack it and assign it to all the
#variables on the left in order
script, filename =argv
#Print a formatted string with the filename from the commandline
print(f"We're going to erase {filename}.")
print("If you dont want that, hit CNTRL-C (^C).")
print("If you do want that, hit RETURN.")
#Requests input in this line
input("?")

print("Opeing the file...")
#Opens the file passed in the commandline to 'write' and assigns
#to variable target
target= open(filename,'w')

print("Truncating the file. Goodbye!")
#This empties the above opened file
target.truncate()
#Describes the next steps
print("Now I'm going to ask you for three lines.")
#Prompts user for line 1 input
line1 = input("line 1: ")
#Prompts user for line 2 input
line2 = input("line 2: ")
#Prompts user for line 3 input
line3 = input("line 3: ")
#Tells what the code in the next few lines is going to do
print("I'm going to write these to the file. ")
#writes line1 into the file
target.write(line1)
#Newline character
target.write("\n")
#Writes line2 into the file
target.write(line2)
#Newline Character
target.write("\n")
#Writes line2 into the file
target.write(line3)
#Newline character
target.write("\n")
#Description of the next step
print("And finally, we close it")
#Closes the file
target.close() 
