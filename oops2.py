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


rohan=student('Rohan',18,'Dhaka')
harry=student('Harry',19,'Sylhet')

rohan.salary=100
rohan.printinfo() #instance variable rohan.salary is accessed via that function
print(rohan.name,harry.name,rohan.age,harry.age,rohan.address,harry.address)
print(student.no_of_students)
rohan.change_no_of_students(1232144)
print(harry.no_of_students)
print(student.no_of_students)





      