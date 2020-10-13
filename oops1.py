class demo:
        
    def __init__(self):
        self.a=10
        self.__b=20
    def display(self):
        print(self.a)
        print(self.__b)
 
    

ob=demo()
ob.display() # OK. Displays 10 and 20
print(ob._demo__b) #Not allowed but can be accessed by name mangling