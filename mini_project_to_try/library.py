from typing import SupportsIndex
import termcolor
class Library:
    def __init__(self,book_category):
        self.books = book_category

    def intro(self):
        message = """\n\t****** Welcome To Anime Vyuh Library ******\n 1. List Of Books\n 2. Request A Book\n 3. Return A Book\n 4. Exit"""
        print(f"\t{message}")

    def listofbooks(self):
        print("\t *** Here Are The List Of Book *** ")
        for index,book in enumerate(self.books,start=1):
            print(f"{index}:{book}")

    def returnbook(self,bookname):
        if bookname not in self.books:
            self.books.append(bookname)
            termcolor.cprint("\nThank You For Returning Book Back",color="green")
            termcolor.cprint(f"{bookname} book is added",color="blue")
        else:
            termcolor.cprint("\nBook Exists",color="yellow")

    def requestbook(self,bookname):
        if bookname in self.books:
            self.books.remove(bookname)
            termcolor.cprint(f"\n{bookname} book is borrowed",color="blue")
            termcolor.cprint("Enjoy Your Read",color="green")
        else:
            termcolor.cprint("\nSorry We Don't Have Such Book",color="yellow")

class Student:
    def __init__(self,id):
        self.usn = id

    def askuser(self):
        ask = int(input("\nEnter Your Choice:"))
        return ask

    def return_book(self):
        request_b = input("\nWhich book could you like to return?")
        return request_b

    def request_book(self):
        borrow = input("\nWhich book could you like to borrow?")
        return borrow

if __name__ == '__main__':
    scan_id = input("Enter your id:")
    student = Student(scan_id)
    books = ['Automate Stuff With Python','EcmaJavascript','ProGit','Java Fundamentals','Arduino With C']
    library_books = Library(books)
    while True:
        try:
            library_books.intro()
            choice = student.askuser()
            if choice in range(1,5):
                if choice == 1:
                    library_books.listofbooks()
                elif choice == 2:
                    library_books.requestbook(student.request_book())
                elif choice == 3:
                    library_books.returnbook(student.return_book())
                elif choice == 4:
                    print("\nThank you for visting! \nHappy Reading")
                    exit()
            else:
                termcolor.cprint("Enter A Valid Choice between (1-4)",color="red")
        except ValueError:
            termcolor.cprint("Invalid Choice",color="red")