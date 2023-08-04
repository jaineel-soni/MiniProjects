welcomeMsg = '''
    =======Welcome to central Library=======
    Please select an option !!
    1--> List all the book
    2--> Request a book
    3--> Add/return a book 
    4--> Exit the library
    '''
print(welcomeMsg)
class library:
    def __init__(self,ListOfBooks):
        self.books = ListOfBooks
    def display_available_books(self):
        print("Books present in this library are ")
        for book in self.books:
            print("*" + book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}.Please keep it safe and return it before 30 days!!")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry this book is currently not available in the library .Kindly wait for few days and then try again.")
            return False
    def returnBook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the books. Hope you enjoy reading the book!!")

class student:
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow ")
        return self.book
    def returnBook(self):
        self.book = input("Enter the name of the book you are returning")
        return self.book 

centralLibrary = library(["Algorithms","Operating System","Data Science"])
std = student()
centralLibrary.display_available_books()
while(True):
   
    a = int(input("Enter a choice : "))
    if a==1:
        centralLibrary.display_available_books()
    elif a==2:
        centralLibrary.borrowBook(std.requestBook())
    elif a==3:
        centralLibrary.returnBook(std.returnBook())
    elif a==4:
        print("Thanks for choosing the central library.")
        exit()
    else:
        print("Invalid choice!!")
