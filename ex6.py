#A syntactic form of a common cs101 joke
#Variable assignment of number of people, note 10 in binary is 2 in base 10
types_of_people=10

#format string with the variale above integrated to the string
x = f"There are {types_of_people} types of people."

#String variable
binary="binary"
#second string variable
do_not="don't"
# string inside string in 2 instances
y=f"Those who know {binary} and those who {do_not}."

#print x and y
print(x)
print(y)
#String inside string number 3
print(f"I said: {x}")
#String inside string #4
print(f"I also said: '{y}'")
#This is a boolean so not a string
hilarious= False
#Boolean inside string
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w= "This is the left side of..."
e="A string with a right side."
print(w + e)
