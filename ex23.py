#Imports library sys
import sys
#Uses argument value from sys and unpacks the variables from the terminal to the
#variables on the left
script, encoding, error = sys.argv

#define this function titled main that takes in 3 arguments
def main(language_file, encoding, errors):
    #reads a line from the language_file, which implies that it is a file
    line = language_file.readline()
    #If a line exists, i.e. True
    if line:
        #Calls the next function print_line() defined below
        #This just gives the first line
        print_line(line, encoding, errors)
        #The line below recursively calls it till no lines are there in the readline
        #Recursion!!!, this gives the big mess below it, because it works
        return main(language_file, encoding, errors)

#Defines another function that takes in three arguments
def print_line(line, encoding, errors):
    #strp() returns a copy of the string with leading and trailing characters removed
    #strip removes white space at the end like \n etc.
    next_lang = line.strip()
    #Encodes the string, this takes in two arguments, encoding scheme as in UTF-8 etc
    #and the error scheme, i.e. strict. Then it is assigned to a variable
    raw_bytes = next_lang.encode(encoding, errors = errors)
    #raw_bites is the utf stuff that is encoded, decoded product are the strings DBES
    #this function decodes the string using the codec(UTF-8 etc) used for encoding then
    #It is assigned to a variable
    cooked_string = raw_bytes.decode(encoding, errors = errors)
    #Prints the encoded string <==> decoded string
    print(raw_bytes,'<==>',cooked_string)

#Opens the file downloaded from Shaw's website and assigns it to the language variable
languages = open("languages.txt", encoding = "utf-8")
#Calls the main function declared initially , that uses the subsequently declared print_line
#function, and this is what prints everything to the display
main(languages, encoding, error)
