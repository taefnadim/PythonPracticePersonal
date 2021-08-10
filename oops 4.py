class student:

    #init to access and change instance variables, sending variables as arguments to the class(), 'self' is the instance
    def __init__(self,aname,aage,aaddress) :
        self.name=aname
        self.age=aage
        self.address=aaddress

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


rohan=student('Rohan',18,'Dhaka')
harry=student('Harry',19,'Sylhet')

class Olevel(student):

    _Protectedvar=19
    __Privatevar=17
    def __init__(self, aname, aage, aaddress,version):
        self.name=aname
        self.age=aage
        self.address=aaddress
        self.version=version
    def printall(self):
        return f"This guy named {self.name} has some issues with his {self.version}"


justin=Olevel('Justin',17,'LA','English')
marques=Olevel('Marques',19,'CA','English')

print(justin.printall())
print(justin.no_of_students)
print(153291-9999)
print(justin._Protectedvar)
print(justin._Olevel__Privatevar)



    