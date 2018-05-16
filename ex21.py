#Functions that return values
#This function takes in 2 arguments, adds them and returns the sum
def add(a, b):
    print(f"ADDING  {a} + {b}")
    #Sum is returned
    return a + b

#This function takes in 2 arguments and returns the difference
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    #The difference is returned
    return a - b
#This function takes in 2 numbers and returns the product
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    #The product is returned
    return a*b
#This function takes in 2 numbers and returns the quotient
def divide(a, b):
    print(f"Divide {a}/{b}")
    #The quotient is returned
    return a/b

print("Let's do some math with just functions!")

#The above mentioned functions are called with appropriate argument values
#And assigned to a variable
#30+5
age = add(30, 5)
#78-4
height = subtract(78,4)
#90*2
weight= multiply(90, 2)
#100/2
iq = divide(100,2)

#Print this formatted string with the above variable values integrated
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

#A puzzle for extra credit, type it in anyway
#Print the statement below
print("Here is the puzzle.")
#Functions assigned to variable.The below statement is called/ executed inside
#out, i.e. divide, multiply,subtract, add in that order
what = add(age, subtract(height, multiply(weight, divide(iq,2))))
#Prints the string below, but I would have put it as a formatted string with {}
print("That becomes: ", what, "Can you do it by hand?")#-4391
#The normal formula is:
print(age+height-((iq/2)*weight))

#My own functions
def circumference(a):
    return round(a*2*3.14159,3)

circum= circumference(10)

print(f"The circumference of a circle with radius 10 units is {circum}")


def temp_convert(a):
    return round((1.8*a)+32,3)
#This messy but I had to typecast for this to run, above fn temp_convert(a)
#Wont run unless the a or temp in this case is typecast to float beacuse 1.8 is
#a float
temp= float(input("Enter a temperature in degrees Celcius: "))
print(f"The fahrenheit equivalent of {temp} is {temp_convert(temp)}")

def BMI_calc(a,b):
    a_kg = float(a)/2.24
    b_cm = (float(b)*2.54)/100
    return round(a_kg/b_cm**2,3)

wgt= input("What is your weight (in lbs) ?: ")
hgt= input("What is your height (in inches) ?")

print(f"Your BMI value is {BMI_calc(wgt,hgt)}")
#Doing the inverse, reverse-engineering the functions 
#My simple formula
print(5+3*10-6)
#The same using the functions is
print(subtract(add(5,multiply(3,10)),6))
