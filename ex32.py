#Create a list with five integers 1 through 5
the_count = [1,2,3,4,5]
#Create a list with 4 fruits
fruits = ['apples','oranges','pears','apricots']
change = [1, 'pennies', 2,'dimes', 3, 'quarters']

#Ths first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#Same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#Also we can go through mixed lists too
#Notice we have to use {} since we do not know what's in it
for i in change:
    print(f"I got {i}")

#We can also build lists, first start with an empty one
elements = []
#This is also possible
#elements = range(6)
#The use range function to do 0 to 5 counts
#Note that range if given as range(a,b), goes from a to b-1
#if you say range(b), it goes from 0,1,2......b-1
for i in range (0,6):
    print(f"Adding {i} to the list")
    #Append is a a function that lists Understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")
