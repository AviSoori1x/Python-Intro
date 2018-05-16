#Import argv from the module sys
from sys import argv
#read the arguments from the commandline and unpack
script, filename = argv
#Open the file given in the commandline and assign it to the
#variable txt
txt= open(filename)
#Print formatted string with the name of the file
print(f"Here's your file {filename}")
#Open the file and print it on the screen/terminal
print(txt.read())
