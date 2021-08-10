
#Return Another function
def fun1():
    def fun2():
        return "This is the second"
    return fun2   

val=fun1() #Variable must be used
print(val()) 

#Assign to variable
def mynum(x):
    return x*5

val2= mynum
print(val2(5))

#Local and Global
x=10
def myfunction():
    global x
    print(x)
    x=7
myfunction()
print(x)

#Closure

def outer(message):
    def inner():
        print('You Entered:',message)
    inner()
outer('Hi')

def passf():
    pass

#Passing Function as arguments
x=8
def function1(b):
    return b+1

def function2(c):
    return c(x)

print(function2(function1))

#VarArgs parameter

def data(Room=5,*Roll,**Phonebook):
    print('They are in', Room)
    print('The Rolls are:')
    for rolls in Roll:
        print(rolls)
    print('The names and phonne numbers are:')
    for name,phones in Phonebook.items():
        print(name,':',phones)
data(1044, 6055,3333,3311, Abid=1234567,Pial=4456767, Khan= 23242344)


#Lambda
a=lambda x,y,z: x+y+z

print(a(4,4,4))

def afun(v):
    return lambda b: v-b

var=afun(0) #function variable
print(var(20))  #lambda variable



def my_decorator(function):
    def takeit():

        var1=function()
        var2=var1.upper()
        return var2
    return takeit

@my_decorator
def sayhello():
    return 'Hello'
print(sayhello())

