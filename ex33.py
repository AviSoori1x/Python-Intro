#Declare the counter variable and set to 0
i = 0
#Create empty list
numbers = []
#Note that you dont have to increment in for loops but you have to increment in
#while loops
#while lop
while i < 6:
    print(f"At the top i is {i}")
    #Adds the number to the end of the list
    numbers.append(i)
    #incremen the counter
    i = i+1
    #print and loop
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")
#Print the numbers one after the other
for num in numbers:
    print(num)
