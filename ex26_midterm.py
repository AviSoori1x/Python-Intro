#Had to import sys from argv because it wasn't there before
from sys import argv
script, filename = argv
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
#Added an input statement that feeds a variable
height = input()
#Fixed the end of the line
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#script, filename = argv
#Fixed the filename spelling
txt = open(filename)

print("Here's your file {filename}:")

#had to correct the file name from tx to txt
print(txt.read())


print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
#had to correct the following line
#Reading the file to stdout,
#You have to read the file object and print. You can't just throw it to print
#Like that
print(txt_again.read())

#Had to throw in an escape character below
print('Let\'s practice everything.')
#Had to throw in """ for multi-line string print
print("""You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.""")


poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#Fixed the " in both the next print statements
print("--------------")
print(poem)
print("--------------")

#Had to fix number
five = 10 - 2 + 3 - 6
#Had to throw in base
print(f"This should be five: {five}")

#Defining function,add colon
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    #Add division operation
    crates = jars/100
    return jelly_beans, jars, crates


start_point = 10000
#Fix this by adding another variable to unpack to
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
#don't add f to format string because .format is already there
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
#Fix the variable name inside the function paranthesis
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
#This is the cleanest way of doing it
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
#Fixed spelling
cats = 30
dogs = 15


if people < cats:
    #Added Paranthesis
    print("Too many cats! The world is doomed!")
#Changed inequality sign
if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")
#Introduced colon after if condition
if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
#Added colon after if condition
if people <= dogs:
    #Print the next " to end the string
    print("People are less than or equal to dogs.")

#equality sign is ==, = is assignment
if people == dogs:
    print("People are dogs.")
