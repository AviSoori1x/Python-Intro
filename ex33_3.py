#Uses function to write a for loop
#Declare the counter variable and set to 0
#Note that you dont have to increment in for loops but you have to increment in
#In for funtion you do not have to increment i or predefine
def forrange(x, num, y):
    for i in range(x):
        print(f"At the top i is {x}")
        #Adds the number to the end of the list
        num.append(i)
        #incremen the counter
        x = x+y
        #print and loop
        print("Numbers now: ", num)
        print(f"At the bottom x is {x}")
    return num
lister=[]
#Always have to convert to the required type
x = int(input("Pick an integer between 0 and 10:\n>"))
y = int(input("Pick an increment between 0 and 10:\n>"))
numbers = forrange(x,lister,y)
print("The numbers: ")
#Print the numbers one after the other
for num in numbers:
    print(num)
