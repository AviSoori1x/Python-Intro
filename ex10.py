#Escape character exercise
#Tabbed in line
tabby_cat="\tI'm tabbed in."
#new line escape in the middle of the line
persian_cat="I'm split\non a line."
#The backslash escapes the backslash
backslash_cat="I'm \\ a \\ cat"
#A long string with multiple tabs and a newline character in the string
fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
#Print all the previously declared and assigned variables
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

drill_var= """
\tThis is tabb\n-ed and that was newline
However, we can \r carriage return like this And
Throw in a back slash like this \\ \nright after
an \' apostrophe
"""

print(drill_var)
