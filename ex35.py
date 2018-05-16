#Import functio exit from module sys
from sys import exit
#Function that takes no arguments
def gold_room():
    print("This room is full of gold, how much do you take?")
    #input#In hindsight, we could use reuse this code to just get a number
    choice = input(">")
    #conditionals
    #What does this even do in python, I know it checks for a number but how?
    if '0' in choice or '1' in choice:
        how_much = int(choice)
    else:
        #calls another function declared below
        dead("Man, learn to type a number.")

    if how_much < 500:
        print("Nice, you're not greedy, you win!")
        #You exit the program, argument of 0 means no error. Anything else is error
        exit(0)
    elif how_much > 500 and how_much < 1000:
        print("You are kind of greedy")
        dead("You shall suffer!!!")
    else:
        #Calls this function again
        dead("You are so greedy. You ought to be ashamed.")
#Calls function bear_room
def bear_room():
    print("There is a bear in here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    #This variable is set to False if this function is called
    bear_moved = False
    #Infinite loop, this is rather confusing
    while True:
        choice = input('>')
        if choice == 'take honey':
            dead("The bear looks at you and slaps your face off.")
            #Boolean combination used, the code is redundant here
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True#This isnt an escape character, Loop runs another time and then you have to type in open door

        elif choice == "taunt bear" and "bear_moved":
            dead("The bear get's pissed off and chews your leg off.")
            #Very interesting, taunt bear has to be typed in for this to execute
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")#No escape character, loops forever

def cthulhu_room():
    print("Here you see the greatest evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input(">")
    #Conditional
    if flee in choice:
    #Function start()
        start()
    elif head in choice:
        dead("Well that was tasty!")
        #when all else fails, run function cthulhu_room()
    else: cthulhu_room()
#Function dead that takes in one argument why
def dead(why):
    print(why, "Good job!")
    exit(0)

#This seems to be the central function that is called at the end
def start():
    print("You are in the dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You manage to escape somehow and live to tell it.")
#The governing function that is called to execute the program
start()
