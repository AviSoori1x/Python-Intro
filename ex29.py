#Declare and assign values to three variables
people = 20
cats = 30
dogs = 15
#Conditionals, do not forget the colon after the expression
if people < cats:
    #This is executed if the expression prior to the colon evaluates to true
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")
#Increments the dogs variable by 5
dogs +=5
#The conditional flow as usual
if people >= dogs:
    print("People are greater than or equal to dogs.")
if people <= dogs:
    print("People are less than or equal to dogs.")
if people == dogs:
    print("People are dogs.")
