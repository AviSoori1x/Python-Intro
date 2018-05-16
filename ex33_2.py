#Uses function to write loop
#Declare the counter variable and set to 0
#Note that you dont have to increment in for loops but you have to increment in
#while loops
#while lop function
def looper(x, num, y):
    i = 0
    while i < x:
        print(f"At the top i is {i}")
        #Adds the number to the end of the list
        num.append(i)
        #incremen the counter
        i = i+y
        #print and loop
        print("Numbers now: ", num)
        print(f"At the bottom i is {i}")
    return num
lister=[]
#Always have to convert to the required type
x = int(input("Pick an integer between 0 and 10:\n>"))
y = int(input("Pick an increment between 0 and 10:\n>"))
numbers = looper(x,lister,y)
print("The numbers: ")
#Print the numbers one after the other
for num in numbers:
    print(num)
