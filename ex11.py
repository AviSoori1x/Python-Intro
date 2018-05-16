#Ask how old the user is, end=' ' is to print on same line
print("How old are you?", end= ' ')
#Request user input
age = input()
#Ask how tall the user is, end=' ' is to print on same line
print("How tall are you?", end= ' ')
#Request user input
height = input()
#Ask how heavy the user is, end=' ' is to print on same line
print("How much do you weight?", end = ' ')
#Request user input
weight = input()
#formattted string with the three previous user input values
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#input takes a string from stdin, this is the other 'form'
input_name=input("What is your name? ")
print(f"It was a pleasure meeting you, {input_name}")
print(input_name,", you are a great man")

#Other ways to use input()

dessert_favorite= input("What is your favorite type of dessert? ")
print("My favorite type of dessert is "+ dessert_favorite + ". It's simply great")
