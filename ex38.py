#Declares variable and assigns sentence
ten_things = "Apples Oranges Crows Telephone Light Sugar"
#Prints sentence like so
print("Wait there are not ten things in that list. Let's fix that.")
#Splits the string variable at the spaces into a list
stuff = ten_things.split(' ')
#['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar']
#Declares a list with the following elements
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#While loop executes while the length of stuff is not equal to 10
while len(stuff) != 10:
    #pop (remove and assign to variable) the last element from the more_stuff list
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    #Adds the last item to the list
    stuff.append(next_one)
    #prints the number of items on the list
    print(f"There are {len(stuff)} items now.")
#Print
print("There we go: ", stuff)

print("Let's do some things with stuff.")
#print the second item in the 'stuff' list
print(stuff[1])
#Print the last item in the stuff list
print(stuff[-1])#whoa, fancy
#removes the last item of the stuff list and prints it
print(stuff.pop())
print(stuff)
#Joins the stuff items with spaces inbetween to a string
print(' '.join(stuff))#what? cool!
#Join the 2nd and the fourth items into a string with # between them
print('#'.join(stuff[3:5]))#super stellar!
