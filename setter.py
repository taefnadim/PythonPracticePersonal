class student:

    #init to access and change instance variables, sending variables as arguments to the class(), 'self' is the instance
    def __init__(self,aname,aage,aaddress) :
        self.name=aname
        self.age=aage
        self.address=aaddress
        #self.email=f"{aname}.{aaddress}@gmail.com"

    #A method that can be called by instance.method(), 'self' is the instance
    def printinfo(self):
        print(self.salary)

    no_of_students=133

    #To change class attribute via a function
    @classmethod
    def change_no_of_students(cls,new_no):
        cls.no_of_students=new_no

    #Alternative Constructor 
    @classmethod
    def alternativeconst(cls,string):
        var=string.split('-')
        print(var)
        return cls(var[0],var[1],var[2])

    #static Method, avoiding 'self'
    @staticmethod
    def printdetails(string):
        print('You wanted to print this via static method',string)
    @property
    def email(self):
        return f"The object is associated with {self.name}, Email: {self.name}.{self.address}@gmail.com"
    



rohan=student('Rohan',18,'Dhaka')
harry=student('Harry',19,'Sylhet')

print(rohan.email)


import inspect

#print(inspect.getmembers(rohan))
print(dir(rohan))