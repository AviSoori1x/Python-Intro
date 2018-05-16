#Prints a string with many lines using the """ """
#We use nested if's in this file. That's what's significant about this!!
print("""You enter a dark room with 3 doors. Do you go through door #1
,door #2 or door #3?
""")
#Get's input from the keyboard and assigns to variable 'door'
door =input(">")
#Executes conditionals
if door == "1" :
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1.Take the cake.")
    print("2.Scream at the bear.")
    #Get's input from the keyboard and assigns to variable 'door'
    bear = input('>')
    #Conditional inside conditional
    if bear == '1':
        print("The bear eats your face off. Good job!")
    #if bear isn't equal to one, but equal to 2
    elif bear == '2':
        print("The bear eats your leg off. Good job!")
    #When all else fails
    else:
        print(f"Well doing {bear} is probably better.")
        print("Bear runs away.")
#if door isnt 1 but 2, run this code
elif door == "2":
    print("You stare into the endelss abyss at Cthulhu's retina")
    print("1.Blueberries")
    print("2.Yellow jacket clothespins.")
    print("3.Understanding revolvers yelling melodies.")
    #Input and assign to this variable titled 'insanity'
    insanity = input('>')
    #if the input above is either 1 or 2, run the code below
    #Note, another conditional inside a conditional
    #Notice the input is considered as a string, hence '' or "" around the numbers
    if insanity == "1" or insanity == '2':
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    #If input isn't any of those, please run this section of code
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

elif door == '3':
    print('You bump into a guy from the IRS.')
    print('He gives you several options:')
    print('1. Pay back the taxes you owe.')
    print("2.Move to Monaco.")
    print("3. Go to jail")
    tax_prob = input("Which option do you go with?: ")

    if tax_prob == '1':
        print("You are being a good citizen.")
    elif tax_prob == '2':
        print("Better buy a plane ticket or charter a plane!")
    else:
        print("Better get a sachet of lube!!")
#the only else to the overarching big if,
else:
    #If anything other than 1 or 2 is pressed, this is what happens.
    print("You stumble around, slip on a banana peel and end up sitting on a throne")
