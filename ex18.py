#Functions start here
#This one is like your scripts with argv
#Note to self: Just curious, is this a pointer?
#The * is because this is in a function, equivalent to argv in the commandline
def print_two(*args):
    #Unpacks the arguments passed on to the function and assigns it to variables
    arg1, arg2 = args
    #Print a formatted string with the arguments entered above
    print(f"arg1: {arg1}, arg2: {arg2}")

#ok, that *args is actually pointless.
#We can just do this, this is what I have seen before
#Pass arguments to a function the usual way, separated by a comma
def print_two_again(arg1, arg2):
    #Print formatted string as usual, with the arguments in the order it's called
    print(f"arg1: {arg1}, arg2: {arg2}")

#This just takes one argument
#Just pass in one argument
def print_one(arg1):
    #Print a formatted string as before but only with one variable
    print(f"arg1: {arg1}")

#This one takes no arguments
def print_none():
    #This is a pointless function for demonstrative purposes only
    print("I got nothin'.")

#Call the first function, note that the arguments passed are strings
print_two("Zed","Shaw")
#Call the second function
print_two_again("Zed", "Shaw")
#Call the third function
print_one("First!")
#Call the fourth and the last function, dont pass arguments in here because the
#function does not take any
print_none()
