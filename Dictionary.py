print("Hello World")

dict1={
    "Name": 'Khan',
    "Age": 18
}

dict1.update({"Address":'Dhaka', "Phone":"01867395212"})
print(dict1.values())
print(dict1.get("Age"))
dict1["Age"]=11
print(len(dict1))
dict1.pop("Phone")
print(dict1)
print(dict1)

def fun1():
    def fun2():
        return "This is the second"
    return fun2   

val=fun1()
print(val()) 