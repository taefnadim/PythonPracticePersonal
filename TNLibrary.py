class library:
    def __init__(self, list_of_books):
        self.allbooks=dict(list_of_books)
    def display(self):
        for i,j in zip(self.allbooks.keys(),self.allbooks.values()):
            print(i, 'is issued by', j)
    def addbooks(self):
        book=input('Enter the bookname:  ')
        self.allbooks.update({book:'None'})
        print('Book Added!')
    def lendable(self):
        print('Enter the book you want to lend:  ')
        count1=0
        count2=0
        lend=input()
        for q in self.allbooks.keys():
            if q==lend:
                count1=count1+1
        if count1>=1:
                for l,m in zip(self.allbooks.keys(),self.allbooks.values()):
                    if l==lend and m!='None':
                        print('Sorry! This book is not available')
                    elif l==lend and m=='None':
                        print('This book is available')
                        name=input('Enter Your Name:  ')
                        for n in self.allbooks.values():
                            if n==name:
                                count2=count2+1
                        if count2>=1:
                            print('Please return your previous book')
                        else:
                            self.allbooks.update({lend:name})
                            print('Book issued successfully')
                            break  
        else:
            print('Not Found')
             
    def returnbook(self):
        print('Enter the bookname you want to return:  ')
        r=input()
        self.allbooks.update({r:'None'})
        print('Book Returned successfully')
           
        
lib=library({'aparajita': 'None','gitanjali':'Karim'})

while 1:
    num = int(input('Enter 1 for display, 2 for Addbook, 3 for Lendbook, 4 for Returnbook, 5 to exit:  '))

    if num == 1:
        lib.display()
    elif num==2:
        lib.addbooks()
    elif num==3:
        lib.lendable()
    elif num==4:
        lib.returnbook()
    elif num==5:
        break
    else:
        print('invalid')
print('Thank you for using this library')

