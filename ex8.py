#Make a string with four curly braces
formatter ="{} {} {} {}"
#Populate the curly braces with numbers 1 through 4
print(formatter.format(1,2,3,4))
#Populate the curly braces with numbers 1 through 4 in words
print(formatter.format("one","two","three","four"))
#Populate the curly braces with the variable 'formatter' itself
print(formatter.format(formatter,formatter,formatter,formatter))
#Populate formatter with the lyrics to the last rap battle from 8 mile
print(formatter.format(
    "His real name is Clarence.\n",
    "His parents have a real great marriage.\n",
    "He went to Cranbrooke,\n",
    "That's a private school!"
))
