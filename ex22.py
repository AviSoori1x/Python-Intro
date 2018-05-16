#This entire file is a list/discussion of symbols. Everything is commented out
#One could think of this as a study guide prior to the midterm in exercise 26
#From exercise 1
# is for commenting stuff out
# print() is to output things onto the screen
# "" and '' are both used to create strings "like this"

#From exercise 2
#Nothing new here, the same stuff as before, mostly about commenting stuff out

#From exercise 3
#You can print mathematical operations inside a print() function,
#often times with a string, and even inside a string as we shall see later
#e.g. print("The string part", variable)
#e.g. print("The string part", 30+50*60)
#e.g. print("The string part", 50>60)#Boolean: False
#Remember PEMDAS but MD and AS are in the same level, left to right

#From Exercise 4
#Assignment to variable can be straight forward or operations
#variable_1= 50
#variable_2= 50* variable1 # you get the idea

#From exercise 5
#round(variable_orl_number_or_operation, number_of_decimal_places)
#formatting string output is very important, here we see f and {}
#var1= 'variable'
#e.g. print(f"This is a string with a variabl included {var1} like this")
#Notice that this wont work without the f or the curly braces {}

#From Exercise 6
#Assigning a boolean like True or False to a variable requires no '' or ""
#They aren't strings
#i.e. booleanvariable= True
#We shall look at the usage of formatting in python code
# Strings can be formatted in the following way in python
#inserted_string= "[[[[[[variable!]]]]]]"
#insert_string = "Here's where I throw the variable in {}"
#print(insert_string.format(inserted_string))
#Output:
#Here's where I throw the variable in [[[[[[variable!]]]]]]
#We can also concatenate two different Strings
#string1 =  "This is the first part of the string"
#string2 =  "This is the second part of the string"
#print(string1+'. '+string2)

#From Exercise 7
#Another example of using formatting
#Remember that f can only be used when there's something inside {}
#Else it's just .format, either or,not both
#print("Mary had a little lamb {}.".format('That smelled really bad'))
#Output:
# Mary had a little lamb That smelled really bad.
#Also you could print a number of the same character(s) like This
#print("*-"*10)
#Output:
#*-*-*-*-*-*-*-*-*-*-
# the end = ' ', character makes sure that it is a space and not a \n at the end
#of each printed string. This could be raher useful
#e.g.
#print('s'+'e'+'x'+'y', end=' ')
#print('s'+'t'+'u'+'f'+'f')
#Output:
#sexy stuff

#From exercise 8
#It is possible to insert multiple strings in the same string with multipe {}
#e.g:
#place_holder = "{} {} {} {}"
#print(place_holder.format('One', 'Two','Three','Four'))
#Output:
#One Two Three Four
#You could include \n character etc. to get them in separate line and so forth

#From exercise 9
#\n is a n escape character to jump into a new line
#You can type variables in with
#random_string= "This is the string to be appended"
#print("I'm going to append a random string like so: ", random_string)
#Output:
#I'm going to append a random string like so:  This is the string to be appended
#Furthermore, with three double string quotes you could print a long string
#taking as much space as you like
#print(
#"""
#This is a really long string
#That proves that
#triple quotes do actually work
#"""
#)

#Output:
#This is a really long string
#That proves that
#triple quotes do actually work

#From exercise 10
#This entire exercise is about escape characters
#\t is for tabbing in by 1 tab or 4 spaces
#\n is for jumping to a new line even in the middle of a string
#\\ is used to print a single '\' character otherwise the interpreter reads it
#as an escape character
#\r is carriage return as in [enter Return] key

#From exercise 11
#This exercise is more about getting input from the user using the input()
#function
#input from the user could be obtained as:
#input1=  input()
#print(input1)
#Output:
#Line one
#Or like this with a prompt in-built as the argument to the function
#input2 = input("Please enter a word:\n> ")
#print(input2)
#Output:
#Genesis

#From exercise 12
#This is merely a repetition of the previous Exercise
#if age, height and weight were declared as variables previously
#one could expect a concatenated string as a response in the case below
#print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#Notice the f for formatting the string1

#From exercise 13
#Here we learn about libraries or modules and these contain various in-built
#functions that the programmer could use
#A typical import expression looks like this:
#from sys import argv
#Here argv is argument value
#argv assignment statement looks like this
#script, argument1, argument2 = argv
#In this expression, what's given in the commandline is unpacked and assigned to
#the variables to the left of the '='.
#These variables can be used in the usual manner

#From Exercise 14
#argv and input could be used together to create useful scripts
#e.g:
#script, one, two argv
#three = input("Give me a string for the third variable: ")
#print(f"This is a string with {one}, {two} and {three} variables")
#Also you can prompt for an input like this i.e. using a prompt
#prompt = "-> "
#myname = input(f"What is your name:\n {prompt}")
#print(f"My name is {myname}")
#Output:
#My name is Avi

#From Exercise 15
#This starts woking with files
#You can pass the filename from the commandline as argv and into a vaiable name
#Opening a file and assigning 'file object' to a variable:
#file1 = open(file_name)
#reading a file and printing to stdout
#print(file1.read())
#You can open the file again and python allows this
#You can close a file as follows
#file1.close()
#This is good practice and better to follow this

#From Exercise 16
#Reading and writing files
#These commands/functions need to be remembered for working with files
#close: closes the file......like file1.close()
#read: reads the file contents and these can be assigned to a variable
#readline: Reads just one line of a text file
#truncate: Empties the file......like file1.truncate()
#write.('stuff'): Writes "stuff" to the file.... like file1.write("I know shit")
#seek(0): Moves the read/write location to the beginning of the file
#open: To open a file in a certain mode.....like file1_object= open(file1, 'w')
#'w' is the default mode of open and it is for writing
#'r' for read
#'a' for append
# These have modifiers with w+,r+ and a+

#From Exercise 17
#More files
#Here we encounter exists() functon which tells if a function exists or not
#exits(file1).....output is true or false
#It is imported as follows
#from os.path import exists
#os.path is a library of some sort
#len(variable) is used to get the length in bytes of a variable
#You can write an entire file to a variable
#infile=open(input_file,'r')
#contents=infile.read()

#From Exercise 18
#Here we start functions
#Functions are code blocks, unbeknownst to the reader, the author has
#introduced numerous inbuilt functions
#read(), write(), exists() etc.
#The skeleton of a function in python is exemplified as thus
#def sample_function(arg1, arg2):
#    number1= arg1
#    number2 =arg2
#    return number1+number2
#print(sample_function(10,20))
#Output:
#30
#You can also pass arguments to functions in this archaic and redundant way
#def function_sample2(*argv):
#    var1, var2 = argv
#    return var1+var2
#print(function_sample2(10,25))
#Note that the variables inside the function are local variables that exist
#inside the function only
#There can be functions that do and do not take in arguments

#From Exercise 19
#We continue with functions
#we can either pass straight values are arguments to a function or
#we can pass variables to which values are assigned
#e.g.: input1 = calc_fun(50,30)
#input2 = calc_fun(num1, num2)
#input3 = calc_fun(num1+20, num2-10)

#From Exercise 20
#The usage of functions could be applied to file manipulations
#if f is the variabe to which a file object is assigned to
#f.seek(0) takes the 'print head' to the start of the file
#f.readline() reads a line from the file till a \n character is encountered
#again end='' is used so that it prints on the same lines

#From Exercise 21
#This also deals with functions
#Functions can return values to the main script
#Again, you evaluate functions insdide out
# Example of a function that returns a value is as follows
#e.g.
#def function_example(a,b):
#    return int(a)+int(b)

#sum1 = function_example(5,10)
#print(sum1)
#Output:
#15
