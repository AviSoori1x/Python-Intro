#This is my own 'game'
#Ask a question after a statement
print("""
What is your favorite car?
1. Lamborghini Huracan
2. Porsche Cayman
3. Lincoln MKZ
""")
preference = input("Please enter the number of the choice you prefer:\n> ")

if preference == '1':
    print("""What color do you like?
    1. Red
    2. Yellow
    3. Silver
    """)
    color1= input('>')
    if color1 == '1':
        print("You like red!")
    elif color1 =='2':
        print("You like yellow!")
    else:
        print("Silver is your choice I see!")
elif preference == '2':
    print("Please don't buy the Cayman, buy the real deal. A 911 perhaps.")
    print("Even a used one would do!")

else:
    print("If you're buying a Lincoln, have you checked out the new Navigator?")
