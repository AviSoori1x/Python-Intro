from sys import argv

script, cmd_temp= argv
#Declares a function that prints out the number of cheese and boxes of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    #Prints the number of cheeses
    print(f"You have {cheese_count} cheeses!")
    #Prints the number of boxes of crackers
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    #Prints an unrelated statement
    print(f"Man that's enough for a party!")
    #Prints another irrelevant line and jumps to a new line
    print("Get a blanket.\n")
command_temp=int(cmd_temp)
#Prompt to explain the usage of the function
print("We can just give the function numbers directly: ")
#Uses the function declared in the first stage
cheese_and_crackers(20,30)

#Another prompt to explain the usage of the same function
print("OR, we can use variables from our script: ")

#Sets two variables and assigns them values as before
amount_of_cheese = 10
amount_of_crackers= 50

#Passes the above declared variables into the function declared initially
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Another prompt to explain the next step
print("We can even do math inside too:")
#Passes arithmetic operations of two numbers as arguments in each slot of the fn
cheese_and_crackers(10+20, 5+6)
#Another explanatory statement printed out to the console
print("And we can combine the two, variables and math: ")
#Calling thr funcion using a mix of variables and mathematical operations
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)


#My function, to convert Fahrenheit to Celcius temperature readings
#Called in 10 different ways with 10 different value combinations

def temp_convert(ftemp):
    ctemp= (5/9)*(ftemp-32)
    return round(ctemp,2)

print (round(temp_convert(98.4),2))

input_temp1=int(input("Please enter a temperature in Fahrenheit, digits only:\n> "))
print("The above entered temperature in Celcius is: ")
print(temp_convert(input_temp1))

print(temp_convert(50+20))

temp3=90
print(temp_convert(temp3))

print(temp_convert(temp3+10))
print(f"Commandline temperature is {cmd_temp}")
print(temp_convert(command_temp))
new_cmd_temp= command_temp+50
print(temp_convert(new_cmd_temp**2))
print(temp_convert(new_cmd_temp*2+55))
print(temp_convert(new_cmd_temp*2+59))
print(temp_convert(new_cmd_temp*5+59))
