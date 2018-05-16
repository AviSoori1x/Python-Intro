#Import argument value from the module/library sys
from sys import argv
#read the arguments from the commandline and unpack
script, user_name, user_age= argv
#declare a prompt string
prompt ='>....>....>'
#A bunch of formatted strings with commandine argument input
print(f"Hi {user_name}, I'm the {script} script.")
print(f"You are {user_age} years old")
print("I'd like to ask you a few questions. ")
print(f"Do you like me {user_name}?")
#prompt for input from inside the script and store in variable
likes =input(prompt)
#prompt for input from within the script and store in variable
print(f"Where do you live {user_name}?")
lives=input(prompt)
#prompt for input from within the script and store in variable
print("What kind of computer do you have?")
computer=input(prompt)
#Print this long string in conclusion which is formatted as usual
print(f"""
Alright, so you said {likes} about liking me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer.
Nice.
""")
