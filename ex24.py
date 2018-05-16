#Print the statement below as a disclaimer
print("Let's practice everything. ")
#\ is used to eascape the 's without finishing off the string
print('You\'d need to know\' bout escapes with \\ that do:')
#newline to start in a newline and tab to indent by four spaces
print('\n newlines and \t tabs')
#Long, multi line string with four " with tab and newline characters inside
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

#prints this as a makeshift boundary
print("--------------")
#prints the above variable
print(poem)
print("--------------")
#Computes five and assigns to variable 'five'
five = 10 - 2 + 3 - 6
#Prints the formatted string with the above declared variable
print(f"This should be five: {five}")
#Start of a new function declaration that takes one argument
def secret_formula(started):
    #Computes number of jelly beans, jars and crates
    jelly_beans = started*500
    jars = jelly_beans/ 1000
    crates = jars/ 100
    return jelly_beans, jars, crates
#Declares a new variable and sets it to 10000
start_point = 10000
#This is very interesting, several things happen Here
#This is also an unpacking thing
#************************************
#The function is used on right to calculate the jelly_beans, jars and crates
#These RETURNED values are unpacked on the left in order.
#The name of the variables in the left are immaterial, order matters
beans, jars, crates = secret_formula(start_point)
#************************************
#remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
#it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

#New value for the starting point for all the bean calculations
start_point = start_point/10

#Print string
print("We can also do that this way:")
#***************************************
#Unpacks the returned variables from the function
formula = secret_formula(start_point)
#This is an easy way to apply a list to a format string, unpacks the variable with
#the pointer like syntax
#Notice the * is used when unpacking a single variable holding several variables like *argv in functions 
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
#***************************************
