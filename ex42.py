## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ##Dog has a name of somekind
        self.name = name
    def bark(self):
        print("Wuff Wuuf")
## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has a name of somekind
        self.name = name
    def purr(self):
        print("Purrr")


##Person is-a object
class Person(object):

    def __init__(self, name):
        ##Person has-a name of some kind
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

    def speak(self):
        print("Speak Queek")
##Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ##Employee has-a __init__ that takes in name, runs the init of a parent class reliably
        super(Employee, self).__init__(name)
        ##Person has a salary of some kind
        self.salary = salary
    def employee_speak(self):
        print("Promote me!!!")

##Fish is-a object
class Fish(object):
    pass

##Salmon is-a Fish
class Salmon(Fish):
    pass

##Halibut is-a Fish
class Halibut(Fish):
    pass

##Rover is-a Dog
rover = Dog("Rover")

##Satan is-a Cat
satan = Cat("Satan")

##Sasan is-a Cat
sasan = Cat("Sasan")

##Jason is-a Cat
jason = Cat("Jason")

##Mary is-a person
mary = Person("Mary")

##mary has-a pet that is satan
#mary.pet= satan

fsal = {
"Baic": 60000,
"Bonus" : 25000,
"Performance Bonus": 30000
}
##Frank is-a Employee with salary 12000, has-a multi-component salary
frank = Employee("Frank", fsal)

##Frank has-a pet that is rover
frank.pet = rover

##flipper is-a Fish
flipper = Fish()

##crouse is-a Salmon
crouse = Salmon()

##harry is-a Halibut
harry = Halibut()

#has-many pets?
mary.pet = [satan, sasan, jason]

#has-many component of salaries
mary.salary = {
    "Baic": 60000,
    "Bonus" : 25000,
    "Performance Bonus": 30000
}




print(frank.salary)
