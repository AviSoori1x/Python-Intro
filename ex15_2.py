#In this script, only use input
#print this string
print("Type the filename again: ")
#Ask for file name again
file_again = input("> ")
#Open the file
txt_again = open(file_again)
#Print this file to the terminal again, just as before
print(txt_again.read())
#txt_again is the file object
txt_again.close()
