# Today We Will try to Build a Library Management System Project:
# print("Library Management System")

class Users:
    def __init__(self, name, roll, password) -> None:
        self.name = name
        self.roll = roll
        self.password = password
        self.borrow_books = []
        self.return_books = []


class Library:
    def __init__(self, book_list) -> None:
        self.book_list = book_list

    def borrow_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if bookName in user.borrow_books:
                    print("First give back your borrowed book")
                    return
                if self.book_list[book] == 0:
                    print("Book already finished")
                    return

                self.book_list[book] -= 1
                user.borrow_books.append(book)
                print("You have borrowed this book successfully")
                return
        print("Book not available")

    def return_book(self, bookName, user):
        for book in self.book_list:
            if book == bookName:
                if book in user.borrow_books:
                    self.book_list[book] += 1
                    user.borrow_books.remove(bookName)
                    user.return_books.append(bookName)
                    print("Book returned Successfully")
                    return

                else:
                    print("Thanks,But I cannot take other guys book")
                    return

        print("This book is Unknown.I can not take this unknown book")

    def availability(self):
        for book in self.book_list:
            if self.book_list[book] > 0:
                print(book, self.book_list[book])

    def donate(self, bookname, amount):
        for book in self.book_list:
            if book == bookname:
                self.book_list[book] += 1
                print("Thanks for donating")
                return
        self.book_list[bookname] = amount
        print("Thank you so much for giving us new types book")


library = Library({"English": 2, "Bangla": 5, "Math": 3})
allUsers = []
currentUser = None

while True:
    if currentUser is None:
        print("Not logged in\nPlease Login or create account(L/C): ")
        option = input()
        if option == "L":
            roll = int(input("Roll: "))
            password = input("password: ")
            match = False
            for user in allUsers:
                if user.roll == roll and user.password == password:
                    currentUser = user
                    match = True
            if match == False:
                print("No user Found")

        else:
            name = input("Name: ")
            roll = int(input("Roll: "))
            password = input("password: ")
            found = False
            for user in allUsers:
                if user.roll == roll:
                    found = True
            if found:
                print("This account already created")
                continue
            user = Users(name, roll, password)
            currentUser = user
            allUsers.append(user)

    else:
        print("\n")
        print("    Option: ")
        print("_________________")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Borrowed book list")
        print("4. Returned book list")
        print("5. Check availability")
        print("6. Donate")
        print("7. Logout")

        print('\n')

        x = int(input("Give Option: "))
        if x == 1:
            book = input("Book Name: ")
            library.borrow_book(book, currentUser)
        elif x == 2:
            book_name = input("Enter book Name: ")
            library.return_book(book_name, currentUser)

        elif x == 3:
            print(currentUser.borrow_books)

        elif x == 4:
            print(currentUser.return_books)

        elif x == 5:
            library.availability()

        elif x == 6:
            bookName = input("Enter your Donate Book: ")
            amount = int(input("Amount: "))
            library.donate(bookName, amount)

        elif x == 7:
            currentUser = None

        print("\n")
""" 
C
jafrul
12
1234

"""
