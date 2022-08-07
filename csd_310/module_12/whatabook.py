from msilib.schema import Error
import sys
import mysql.connector
from mysql.connector import errorcode

#After not being able to get my original code operating I used some of the formatting and code in the csd-310 GitHub to complete the program.
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#creating the user menu
def show_menu():
    print("\n -- Main Menu --")
    print("   1. View Books\n   2. View Store Locations\n   3. My Account\n   4 Exit Program")

    try:
        choice = int(input(' Please select a choice from the menu '))

        return choice
    except ValueError:
        print(" Invalid Choice, please try again")

        sys.exit(0)

#creating the book menu
def show_books(_cursor):
    #Query for all the book data
    _cursor.execute("SELECT book_id, book_name, author, details from book")

    books = _cursor.fetchall()

    print("\n  BOOK LIST")

    for book in books:
        print(" Book Name: {}\n Author: {}\n Details: {}\n".format(book[0], book[1], book[2]))

#creating the location menu

def location(_cursor):
   _cursor.execute("SELECT store_id, locale from store")
   locations = _cursor.fetchall()

   print("\n WHATABOOK STORE LOCATIONS")

   for location in locations:
    print("Local: {}\n".format(location[1])) 

#confirming the user

def confirm_user ():
    try:
        user_id = int(input("\n  Enter in a customer ID number"))

        if user_id < 0 or user_id > 3:
            print("Incorrect customer ID number, please try again")
            sys.exit(0)
        else:
            return user_id
    except ValueError:
            print("\n Invalid customer ID, please try again")

            sys.exit(0)

#Creating a function to show the Menu
def show_account_menu():
    try:
        print("WhatABook Menu")
        print(" 1. Wishlist\n   2. Add Book\n    3. Main Menu")
        account_option = int(input(" Please select option from our menu: "))

        return account_option


    except ValueError:
        print("Invalid choice, please try again")

        sys.exit(0)

#creating a query for the database
def show_wishlist(_cursor, user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(user_id))

    wishlist = _cursor.fetchall()

    print ("\n WISHLIST ITEMS")

    for book in wishlist:
        print("Book Name: {}\n   Author:{}\n".format(book[3], book[4], book[5]))

#creating a query for list of books not on the wishlist

def show_other_books(_cursor, _user_id):

    query = ("SELECT book_id, book_name, author, details"
    "FROM book"
    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id)) 

    print(query)

    _cursor.execute(query)

    show_other_book = _cursor.fetchall()

    print("BOOKS AVAILABLE TO ADD TO WISHLIST")

    for book in show_other_book:
        print("Book ID: {}\n   Book Name: {}\n".format(book[0], book[1]))

def wishlist_addition(_cursor, _user_id, _book_id):
    _cursor.execute("Add to wishlist(user_id, book_id VALUES({}, {})".format(_user_id, _book_id))

#Code to check database errors

try:

    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    print("Welcome to WhatABook App!")

    user_option = show_menu()  #calling the function to show user the menu

    account = show_account_menu

    while user_option !=4:
        if user_option == 1:   #calling the show_books function if user selects it
            show_books(cursor)

        if user_option ==2:     #calling the location function if user selects it
            location(cursor)

        if user_option ==3:    #calling the account function to run
            user_id_selection = confirm_user()
            account = show_account_menu()

        while account != 3:

            if account == 1:
                show_wishlist(cursor, user_id_selection)

            if account == 2:
                show_other_books(cursor,user_id_selection)

                book_id = int(input ("Enter the ID of the book you wish to add to your wishlist"))
                        
                wishlist_addition(cursor, user_id_selection, book_id)
                
                db.commit()

                print("\n Book ID: {}  has successfully been added to your wishlist".format(book_id))

            if account < 0 or account > 3:
                print (" Incorrect option selection, please try again")

            account = show_account_menu()

        if user_id_selection < 0 or user_id_selection > 4:
            print("\n Incorrect option selected, please try again")

        user_id_selection = show_menu()

    print("WhatABook program complete, the application will now close, thank you for using our application")


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("    THe specified database does not exist")

    else:
        print(err)

finally:
     db.close