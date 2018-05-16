#Extremely important, comment everything and understand everythings
#Import random module
import random
#import urlopen function from urllib.request library
from urllib.request import urlopen
#import sys module
import sys

#Assign WORD_URL to the URL given below, this has the words.txt file
WORD_URL = "http://learncodethehardway.org/words.txt"
#Create an empty list called WORDS
WORDS = []
#I think the core issue is that the %%%, @@@ and *** are string format characters
#from python 2.x that were carried over to 3.x. Usually f strings are used - maybe not

#This is a dictionary with placeholders %%%, *** and @@@
PHRASES = {

    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
     #escape characters, newline and tab
    "class %%%(object):\n\tdef __init__(self, ***)":
     "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
     "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
     "set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
}

#do they want to drill phrases first
#If we pass "english" as an argument, the Phrase comes first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False
#Load up the words from the website

#The method readlines() reads until EOF using readline()
#and returns a list containing the lines
#This iterates over the words in the text file.
#Note that each line that is read is a separate word
for word in urlopen(WORD_URL).readlines():
    #str: This returns a string version of the object with the given encoding
    #So this basically fills up the WORDS list with words
    #for strip: If the chars argument is not provided,
    # all leading and trailing whitespaces are removed from the string.
    WORDS.append(str(word.strip(), encoding = "utf-8"))
    #So we fill up the words list in the above line
def convert(snippet, phrase):
    #This defines the class names
    #The capitalize fn returns a copy of the string
    #with its first character capitalized and the rest lowercased.
#random.sample(population, k)
#Return a k length list of unique elements chosen from
#the population sequence or set. Used for random sampling without replacement
#These are the class names, so class names go where %%% is
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
#Other names go where *** is
    other_names =  random.sample(WORDS, snippet.count("***"))
    #Creates two empty lists
    results = []
    param_names = []
#count counts the number of argument strings
    for i in range(0, snippet.count("@@@")):
        #Picks a random integer from 1,2,3, so the number of parameters is varied
        param_count = random.randint(1,3)
    #str.join(sequence)
    #The method join() returns a string in which the string elements
    # of sequence have been joined by str separator
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
#Iterate over two lists
    for sentence in snippet, phrase:
        #[:] python way of copying a list 
        result = sentence[:]

        #fake class names
        for word in class_names:
            result = result.replace("%%%",word,1)
        #fake other names
        for word in other_names:
            result = result.replace("***",word,1)
        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word,1)

        results.append(result)

    return results
    #Keep going until they hit CNTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)
#Loops through list
        for snippet in snippets:
            phrase = PHRASES[snippet]
            #calls convert function to get question, answer
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                #Hack to swap things
                question, answer = answer, question
            print(question)

            input('>')
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
