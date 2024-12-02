

# Library Management App

import os
import csv

print("Welcome to Library Management System app\n")
books = []
properties = ["title", "author", "isbn", "year", "price", "quantity"]


def load_from_database():
    global books
    if os.path.exists("all_books.csv"):
        with open("all_books.csv", "r") as read_file:  # check if file exists
            content = csv.reader(read_file)
            books.clear()
            for row in content:
                books.append(row)

    else:
        print("all_books.csv file not found! try adding some book(s)\n")


def show_books():
    global books
    if len(books) < 2:
        print("list is empty, try adding some\n")
    else:
        for i in range(0, len(books)):
            if i == 0:
                print("  ", books[0])
            else:
                print(f"{i})", books[i])
        print()


book = {
    'title': 'title',
    'author': 'author',
    'isbn': 123,
    'year': 123,
    'price': 0.50,
    'quantity': 1,
}


def input_book():
    book["title"] = input("Enter Book Title (string): ")
    book["author"] = input("Enter Author(s) (string): ")
    book["isbn"] = int(input("Enter ISBN (number): "))
    book["year"] = int(input("Enter Publishing Year (number): "))  # to update: implement try except
    book["price"] = float(input("Enter Book Price (float): "))
    book["quantity"] = int(input("Enter Quantity (number): "))


def save_it():
    global books
    new_book = []
    input_book()
    if len(books) == 0:
        books.append(properties)
    for value in book.values():
        new_book.append(value)
    books.append(new_book)
    with open("all_books.csv", mode="w", newline='') as write_file:
        csv_writer = csv.writer(write_file)
        csv_writer.writerow(properties)
        for i in range(1, len(books)):
            csv_writer.writerow(books[i])

    load_from_database()
    print("Book added to database!\n")


def edit_it():
    global books
    new_book = []
    if len(books) < 2:
        print("Book list is empty so you cant edit any. add some book(s) first")
    else:
        print("The Book list is : ")
        show_books()
        select = int(input("Select the number from the above list, which you want to edit : "))
        if 1 <= select <= len(books):
            input_book()
            for value in book.values():
                new_book.append(value)
            books[select] = new_book
            with open("all_books.csv", mode="w", newline='') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(properties)
                for i in range(1, len(books)):
                    csv_writer.writerow(books[i])

            print(f"Book {select} edited in database!\n")
        else:
            print("invalid choice, try again.\n")


def remove_it():
    global books
    if len(books) < 2:
        print("Book list is empty so you cant remove any. add some book(s) first")
    else:
        print("The Book list is : ")
        show_books()
        select = int(input("Select the number from the above list, which you want to delete : "))
        if 1 <= select <= len(books):
            # remove at index:
            books.pop(select)
            # remove from database:
            with open("all_books.csv", mode="w", newline='') as write_file:
                csv_writer = csv.writer(write_file)
                csv_writer.writerow(properties)
                for i in range(1, len(books)):
                    csv_writer.writerow(books[i])

            print(f"Book {select} removed from database!\n")
        else:
            print("invalid choice, try again.\n")


while True:
    print("Please select an option from below : ")
    print("0. close app")
    print("1. view all books info from database")  # from all_books.csv file
    print("2. add new book to database")
    print("3. edit a book info in database")
    print("4. remove a book info from database")
    print()
    selected = input("please enter a choice : ")

    if selected == "0":
        print("Thank You for using our Library Management System app")
        break

    elif selected == "1":
        load_from_database()
        show_books()

    elif selected == "2":
        save_it()

    elif selected == "3":
        edit_it()

    elif selected == "4":
        remove_it()

    else:
        print("invalid choice, please try again\n")
