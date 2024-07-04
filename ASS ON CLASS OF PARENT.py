class Parent():
    def __init__(self, lastName, complexion, tribalMark):
        self.name= lastName
        self.color= complexion
        self.mark= tribalMark
    def general(self):
        print(f"my surname is {self.name}, I'm {self.color} in complexion and has a tribal mark called {self.mark}")
    
class Child(Parent):
    def __init__(self, lastName, complexion, tribalMark, weight):
        super().__init__(lastName, complexion, tribalMark)
        self.weight= weight
    def child(self):
        print(f"my surname is {self.name}, I'm {self.color} in complexion, with a {self.weight} weight and a tribal mark called {self.mark}")
        
class Grandchild(Child):
    def __init__(self, lastName, complexion, tribalMark, weight, manner):
        super().__init__(lastName, complexion, tribalMark,weight)
        self.manner= manner
    def grand(self):
        print(f"Her surname is {self.name}, {self.color}, {self.weight} and very {self.manner}")

person1= Parent(lastName="Oladimeji", complexion="dark", tribalMark="Pele")
person2= Child(lastName="Tomori", complexion="fair", tribalMark="Baamu", weight="fat")
person3= Grandchild(lastName="Musa", complexion="light", tribalMark="Gonbo", weight="slim", manner="rude")

person1.general()
person2.child()
person3.grand()