class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailbleBooks(self):
        print('Books present in this liberary are: ')
        for book in self.books:
            print('\t' + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f'You have been issued {bookName}.\nHandle safely and return on time 😊.')
            self.books.remove(bookName)
            return True
        else:
            print('This book is unavailable 😒. Check out other books 😜.')
            return False

    def returnBook(self, bookName):         
        self.books.append(bookName)
        print('Thanks for the book!😁 Check out our books 😜.')
        
class Student:
    def requestBook(self):
        self.book = input('Enter the name of the book: ')
        return self.book

    def returnBook(self):
        self.book = input('Enter the name of the book to be returned: ')
        return self.book
        

if __name__ == '__main__':
    centralLibrary = Library(['Algorithms', 'Django', 'Clrs', 'Python Notes'])
    student = Student()
    # centralLibrary.displayAvailbleBooks()

    while (True):
        welcomeMsg = '''\n=======Welcome to Central Library=======
        Choose an option:
        Press 1 to see the list of all the books
        Press 2 to request a book
        Press 3 to return/donate a book
        Press 4 to exit the Library'''
        print(welcomeMsg)

        try:
            a = int(input('Enter an option: '))
            if a == 1:
                centralLibrary.displayAvailbleBooks()
            elif a == 2:
                centralLibrary.borrowBook(student.requestBook())
            elif a == 3:
                centralLibrary.returnBook(student.returnBook())
            elif a == 4:
                exit()
            else:
                print('Invalid Choice')
        finally:
            print('Thanks for choosing Central Library 😃')
    