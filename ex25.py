#This is a list of functions
#This function breaks words at the space. It takes in one argument
def break_words(stuff):
    """This function will break up words for us."""
    #This splits a string into segments at the spaces
    words = stuff.split(' ')
    #Returns the string variables
    return words

#This function takes in one argument and returns a list of sorted words in
#Alphabetical order
def sort_words(words):
    """Sorts the words"""
    #function sorted does the alphabetical sorting
    return sorted(words)

#Function that takes in one argument is declared
def print_first_word(words):
    """Prints the first word after popping it off."""
    #Pop returns and removes the first item in the list
    word = words.pop(0)
    #Prints the thus returned word
    print(word)

#Function that takes in one argument is declared
def print_last_word(words):
    """Prints the last word after popping it off"""
#*******************************
    #Returns and removes the last word in the string
#-1 used as an index gives the last item
    word = words.pop(-1)
    print(word)

#Function that takes in one argument is declared
def sort_sentence(sentence):
    """Takes in a full sentences and returns the sorted words"""
    #Uses previously declared function
    words = break_words(sentence)
    return sort_words(words)
#Function that takes in one argument is declared
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    #Uses previously declared function
    words = break_words(sentence)
    #Uses previously declared function
    print_first_word(words)
    #Uses previously declared function
    print_last_word(words)
#Function that takes in one argument is declared
def print_first_and_last_sorted(sentence):
    """Sorts the words and prints the first and last one"""
    #Uses previously declared function
    words =  sort_sentence(sentence)
    #Uses previously declared function
    print_first_word(words)
    #Uses previously declared function
    print_last_word(words)
