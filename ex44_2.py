#Defines class Parent
class Parent(object):
    #mthd override inside Parent
    def override(self):
        print("PARENT override()")
    #mthd implicit inside Parent
    def implicit(self):
        print("PARENT implicit()")
    #mthd altered inside altered
    def altered(self):
        print("PARENT altered()")
#Defiles class Child
class Child(Parent):
    #mthd override inside Child
    def override(self):
        print("CHILD override()")
    #mthd altered inside Child
    def altered(self):
        print("CHILD BEFORE PARENT altered()")
        #super gets you the thing from the parent class
        super(Child,self).altered()
        print("CHILD AFTER PARENT altered()")
#Create two instances
dad = Parent()
son = Child()

dad.implicit()#PARENT implicit()
son.implicit()#PARENT implicit()

dad.override()#PARENT override()
son.override()#CHILD override()

dad.altered()#PARENT altered()
son.altered()
#CHILD BEFORE PARENT altered()
#PARENT altered()
#CHILD AFTER PARENT altered()
