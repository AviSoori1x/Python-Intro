#mystuff = {'apple': "I AM APPLES!"}
#print(mystuff['apple'])

#def apple():
#    print("I AM APPLES!")

#This is just a variable
#tangerine = "Living reflection of a dream"

#import mystuff
#mystuff.apple()
#print(mystuff.tangerine)


#Define a new class
class MyStuff(object):
    #there has to be two underscores on either side of the init
    def __init__(self):
        self.tangerine = "And now a thosand years between"
    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)

#Dict style
#mystuff['apples']

#module style
#mystuff.apples()
#print('mystuff.tangerine')

#Class style
#thing = MyStuff()
#thing.apples()
#print(thing.tangerine)
