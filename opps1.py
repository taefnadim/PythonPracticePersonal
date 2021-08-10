class Student:
    default_salary=901
    pass

#Instances
rohan=Student()
harry=Student()

#Instance variables
rohan.salary=50
harry.salary=60

#Changing class attribute via instance which just actually creates another instance variable
harry.default_salary=90111

print(rohan.salary, harry.salary,Student.default_salary, harry.default_salary,rohan.default_salary)#See! only harry.default_salary has been updated
print(harry.__dict__)
print(Student.__dict__)