#Declares variables and assigns numbers
people = 30
cars = 40
trucks = 15
#Conditionals
if cars > people:
    print('We should take the cars.')
#If above didn't workout, what's this ....elise if almost
elif cars < people:
    print("We should not take the cars.")
    #Base case, after if and however many elif's you get else
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks. ")

elif  trucks > cars:
    print("Elif maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if cars + people > trucks and cars > people:
    print("The complicated boolean was evaluated")
elif cars + people > trucks and cars < people:
    print("Then this evaluated")
else:
    print("Finally finished it")
