#Exercise: Functions and files
#imports the argument value from module/ library sys
from sys import argv
#Unpack the argument value input from the commandline to the variables on the left
script, input_file = argv

#First function, which reads the file
def print_all(f):
    print(f.read(), end="")

#This function takes the 'cursor'position back to the start of the file i.e. rwd
def rewind(f):
    f.seek(0)

#This function prints a line against the position of the file
def print_a_line(line_count, f):
    print(line_count, f.readline(), end ="")

#Opens the input_file from the commandline input and assigns it to current_file
#You have to open the file for any of the functions to be useful, i.e. to work
current_file = open(input_file)

#Prints this explanatory statement
print("First let's print the whole file:\n")

#Prints the entire contents of the input file
print_all(current_file)

#Explanatory statement
print("Now let's rewind, kind of like a tape.")
#Takes the cursor back to the beginning of the file
rewind(current_file)

#Another statement explaining what we are doing
print("Let's print three lines: ")
#Variable assignment getting the current line
current_line = 1
#current_line is 1 now
#Prints this line from the above mentioned folder against the line number 1
print_a_line(current_line, current_file)

#Variable assignment getting the subsequent line
current_line = current_line + 1
#current_line is 2 now
#Prints that line against the line number
print_a_line(current_line, current_file)
#Gets the next line and again updates the variable
current_line = current_line + 1
#current_line is 3 now
#Prints this line against the line number
print_a_line(current_line, current_file)
#I believe the file is automatically closed
#The following line was not in the original script
current_file.close()
