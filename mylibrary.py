class library:
    def __init__(self, *list_of_books):
        self.list_of_books=list(list_of_books)
        self.lenders_dict=dict.fromkeys(self.list_of_books, 'Not taken')

    def displaybooks(self):
        print("The available books are: ")
        for i in self.lenders_dict.keys:
            print(i)

    def displaylenders(self):
        print("The bookes that has been lended already: ")
        for valuee in self.lenders_dict.values:
            print(valuee)

    def addbooks(self):
        book=input('Enter new book name: ')
        self.lenders_dict.update({book:None})
        print("Book added!")





lib=library('AGRADUT')
def main():
    while 1:
        choice=input('Enter the choice in lower:')
        if choice== "displaybook":
            lib.displaybooks()
        elif choice=="addbooks":
            lib.addbooks()
        elif choice=="lenders":
            lib.displaylenders()
main()


        


        