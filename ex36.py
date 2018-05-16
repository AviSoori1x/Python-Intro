from sys import exit
#define start function
def start():
#Ask for age
    value_age = input("What is your age? ")
    age = verify_age(value_age)

    if age < 18:
        print("We cannot be held liable to injury.\n We suggest you try another travel agent")
        exit(0)
    else:
        print("""Plese choose an income level:
        1: less than $50,000 per annum
        2.: $50,000 to $100,000 per annum
        3. >$100,000 per annum
        Plese make sure to only enter a number
        """)
        income_ask()

#How to only get a number
#**********************************************************************
def verify_age(age):
    try:
        return int(age)
    except ValueError:
        try:
            return float(income)
        except:
            print("Enter a valid age on next attemp.")
            exit(0)
#**********************************************************************
def verify_income(income):
    try:
        return int(income)
    except ValueError:
        try:
            return float(income)
        except ValueError:
            print("Enter a number on next attempt")
            income_ask()
#************************************************************************
def income_ask():
    income = input(">")
    income_level=verify_income(income)
    if income_level == 1:
        Asia()
    elif income_level==2:
        North_America()
    elif income_level==3:
        Europe()
    else:
        print("Please enter one of the above three choices. i.e. 1, 2 or 3.")
        income_ask()
#************************************************************************
def Asia():
    Place = input("Where do you want to go in Asia? (Enter country)\n>")
    if Place !='North Korea':
        print(f"Sure we'll take you to {Place}")
        exit(0)
    else:
        exit_func()

def Europe():
    Place = input("Where do you want to go in Europe? (Enter country)\n> ")
    if Place !='Neverland':
        print(f"Sure we'll take you to {Place}")
        exit(0)
    else:
        exit_func()

def North_America():
        Place = input("Where do you want to go in North America? (Enter country)\n>")
        if Place !='Nicaragua':
            print(f"Sure we'll take you to {Place}")
            exit(0)
        else:
            exit_func()

def exit_func():
    print("We're afraid that we cannot make that happen. Good luck!")
    exit(0)
start()
#Ask for income level
#Route to different continent functions
