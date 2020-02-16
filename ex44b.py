class Parent(object): # define a class

    def override(self): #def function inside class
        print("PARENT override()") # prints something

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent): # inherits Parent class

    def override(self): # def function override
        print("CHILD override()")

    def altered(self): # def function altered
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered() # 
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
