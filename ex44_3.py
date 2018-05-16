class Other(object):

    def override(self):
        print("OTHER override() ")

    def implicit(self):
        print("OTHER implicit() ")

    def altered(self):
        print("OTHER altered() ")

class Child(object):

    def __init__(self):
        #Where composition kicks in
        self.other = Other()

    def implicit(self):
        #Where you get the has-a relationship
        self.other.implicit()

    def override(self):
        print("CHILD override() ")

    def altered(self):
        print("CHILD, BEFORE OTHER altered() ")
        #Where the composition is utilized to call a  function from other class
        self.other.altered()
        print("CHILD, AFTER OTHER altered() ")


#Instantiation of son instance of the class Child()
son =  Child()
son.implicit()#OTHER implicit()
son.override()#CHILD override()
son.altered()
#CHILD, BEFORE OTHER altered()
#OTHER altered()
#CHILD, AFTER OTHER altered()
