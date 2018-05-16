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
txt.close()
#print this string
print("Type the filename again: ")
#Ask for file name again
file_again = input("> ")
#Open the file
txt_again = open(file_again)
#Print this file to the terminal again, just as before
print(txt_again.read())
txt_again.close()
