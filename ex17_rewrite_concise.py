#####Matched Z. Shaw
#Imports argument value from sys
#Imports exists from os.path module


#Reads the script, from file and to file from the command line in to the variables on the left


#Prints this formatted file to indicate data flow


###We could do these on one line, how?
#Opens the from file and assigns to variable
#Reads the file contents into new variable
#indata = open(from_file).read()

#Prints the length of the file in bytes

#Open a file for 'writing' and assign to variable out_file
#out_file = open(to_file, 'w')
#Writes the data read from that file to new file
#standard out

from sys import argv;from os.path import exists; script, from_file, to_file = argv; print(f"Copying from {from_file} to {to_file}"); print(f"The input file is {len(open(from_file).read())} bytes long\nDoes the output file exist? {exists(to_file)}");open(to_file, 'w').write(open(from_file).read());print("Alright, all done.")
