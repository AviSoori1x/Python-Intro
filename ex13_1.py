#import argv from the module sys
from sys import argv
#this is the do it yourself part with one fewer variable
# read the WYSS section for how to run this
#the line below does the following:
#Take whatever is in argv, unpack it and assign it to all the
#variables on the left in order
script, first, second =argv
#print second argument
print("Your first variable is:",first)
#print third argument
print("Your second variable is:",second)
#print first argument
print("Your third variable is:", script)
