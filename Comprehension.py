n=int(input('Enter the num: '))
list1=[]

for i in range(n):
    list1.append(input(f'Enter the element no. {i+1}'))

print(list1)

set1={i for i in list1 }
dict1={ i: i for i in list1 }
tuple1=(i for i in list1)
print(set1)
print(dict1)
print(type(tuple1))