class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

#Implicit inheritance
dad.implicit()
#So when you call the implicit method in son, which is only def in parent
#it prints
son.implicit()


#Override explicitly
class Physician(object):
    def implicit(self):
        print("Physician implicit()")

class Surgeon(Physician):
    def implicit(self):
        print("Surgeon implicit()")

Jim = Physician()
Susan = Surgeon()

Jim.implicit()

Susan.implicit()
