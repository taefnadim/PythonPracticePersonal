class amarclass:
    companyname= 'RFL' #Attributes

    def __init__(self,course,duration):  #default init method for initializing attribute, Self is default
        self.course=course
        self.duration=duration

    def printinfo(self):   #Method
        print('This is', amarclass.companyname)


var1=amarclass('Etai Course bujhla',19)
var2=amarclass('Etai Course bujhla hmm',7)
var1.printinfo() #Accessing methods
var2.printinfo()

print(var1.course,'has',var1.duration) #Accessing attributes
del var1.duration
var1.course='HTML'
print(var1.course)
