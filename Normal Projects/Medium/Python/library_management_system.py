# Mini project-1 (OOP's Library)

# book_list = []
#
# def display_books():
#     for i,j in enumerate(book_list):
#         print(i,j)
#
# def lend_books():
#     book_name = input("Enter the book name :")
#     book_list.remove(book_name)
#     return display_books()
#
# def donate_book():
#     book_name = input("Enter book name : ")
#     if book_name not in book_list:
#         print("Thanks for donating.\n")
#         return book_list.append(book_name)
#     else:
#         print(f"{book_name} already in stock.")
#
# def return_book():
#     book_name = input("Enter book name : ")
#     if book_name not in book_list:
#         print("Thanks for returning the book. Hope you enjoy it!!!\n")
#         return book_list.append(book_name)
#     else:
#         print(f"{book_name} already in stock.")
#
# while True:
#     print("-----Welcome to OOP's Library-----")
#     print(''' 1. Display books \n 2. Lend books \n 3. Donate books \n 4. Return book \n 5. Exit library \n''')
#     user_input = int(input("Enter your choice : "))
#
#     if user_input ==  1:
#         display_books()
#         continue
#     elif user_input == 2:
#         lend_books()
#         continue
#     elif user_input == 3:
#         donate_book()
#         continue
#     elif user_input == 4:
#         return_book()
#         continue
#     elif user_input == 5:
#         break
#     else:
#         print("Enter a valid input")
#
# print("Thanks for using our library")


# From CodeWithHarry
class Library:
    def __init__(self,name,books):
        self.name = name
        self.dictionary = books
        self.lend_list = {}

    def display_books(self):
        print("We have these books :\n")
        for books in self.dictionary:
            print(books)
        print("\n")

    def lend_books(self):
        book_name = input("Enter your book name : ")
        if book_name not in self.dictionary:
            print(f"Sorry!!! This book has already taken by {self.lend_list.get(book_name)}")
        else :
            user_name = input("Enter your name : ")
            self.lend_list.update({book_name:user_name})
            self.dictionary.remove(book_name)
            print("Book lended successfully!!!")
        print("\n")

    def add_book(self):
        book_name = input("Enter your book name : ")
        if book_name not in self.dictionary :
            self.dictionary.append(book_name)
            print("Thanks for giving ")
        else :
            print("This book is already available in our library.")
        print("\n")

    def return_book(self):
        book_name = input("Enter your book name : ")
        if book_name not in self.lend_list:
            print("This book is not lended.")
        else:
            self.lend_list.pop(book_name)
            self.dictionary.append(book_name)
        print("\n")

if __name__ == '__main__':

    OOP = Library("OOP's Library",["Python","C++","Javascript","Java","Swift","Student's Hack"])

    while True:
        print("-----Welcome to OOP's Library-----")
        print(" 1.Diplay Books \n 2.Lend Book \n 3.Add Book \n 4. Return Book \n 5.Exit Library \n")
        user_input = int(input("Enter your choice : "))

        if user_input == 1:
            OOP.display_books()
        elif user_input == 2:
            OOP.lend_books()
        elif user_input == 3:
            OOP.add_book()
        elif user_input == 4:
            OOP.return_book()
        elif user_input == 5:
            exit()
        else:
            print("Enter a valid input.\n")