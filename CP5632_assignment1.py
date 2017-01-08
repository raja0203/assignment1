"""
NAME : RAJA VIGNESH VIRKUDI RAGHUNATH
DATE : 06/01/2017
PROGRAM DETAILS : This program is a simple reading list where we create an empty list BOOK_LIST and perform read,write operations to the CSV file /
                 Along with,two more operations Add and mark book functions. Program functions as per the users input and performs operations based
                 on the required User inputs.
GITHUB LINK     :   https://github.com/raja0203/assignment1.git

PSEUDO CODE:
start
BOOK_FILE = "books.csv"
FUNCTION main():
    display "Reading List 1.0 - by Raja Vignesh Virkudi Raghunath"
    get name
    book_list = []
    load_books(book_list)
    display menu
    get choice
    while choice != Q
        if choice == R
            display "List Require books"
        elif choice == C
            display "List Completed books"
        elif choice == A
            display "Add new book"
        elif choice == M
            display "Mark a book as completed"
        else
            display invalid message
        display menu
        get choice
    display "Have a nice day :)" message

FUNCTION display_menu():
    display "menu:"
    display "R - List required books"
    display "C - List completed books"
    display "A - Add new book"
    display "M - Mark a book as completed"
    display "Q - Quit"
    display()
ENDFUNCTION

FUNCTION load_books(book_list):
''' This function is for display of lines from file '''
    file = open(BOOK_FILE, 'r')
        for line in file:
            book_list.append(line.strip().split(','))
ENDFUNCTION

FUNCTION list_completed_books(book_list):
''' This function is to list completed books '''
    total_no_pages = 0
    flag = 0
    count = 0
    print("Completed books:")
    for book in book_list:
        IF book[3] == 'c':
            display "{}. {} by {} {} pages".format(count, book[0], book[1], book[2])
            total_no_pages += int(book[2])
            flag += 1
        count += 1
    display "Total number of pages for {} books: {}".format(flag, total_no_pages)
ENDFUNCTION
main()
end

"""
__author__ = "Raja Vignesh Virkudi Raghunath"

# Initialize the constants
BOOK_FILE = "books.csv"


def main():
    print('Reading List 1.0 - by Raja Vignesh Virkudi Raghunath')
    book_list = []
    load_books(book_list)
    display_menu()
    choice = input('>>>').upper()
    while choice != 'Q':
        if choice == 'R':
            list_required_books(book_list)
        elif choice == 'C':
            list_completed_books(book_list)
        elif choice == 'A':
            book_list = add_new_book()
        elif choice == 'M':
            mark_book_completed(book_list)
        else:
            print('Please enter R, C, A, M or Q(uit) ')
        display_menu()
        choice = input('>>>').upper()
    print('Have a nice day :) ')


def display_menu():
    """
    :return:Menu with Choice
    """
    # print the menu
    print("menu:")
    print("R - List required books")
    print("C - List completed books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
    print()


def load_books(book_list):  # Loading books from file to list
    """
    :param book_list: The book list
    :return:Reads line from file
    """
    file = open(BOOK_FILE, 'r')
    for line in file:
        book_list.append(line.strip().split(','))


# end of load_books()
def list_required_books(book_list):  # Required books function declaration
    """
    :param book_list: The book list
    :return: The list of Required books
    """
    total_no_pages = 0
    flag = 0
    count = 0
    print("Required books:")
    for book in book_list:
        if book[3] == 'r':
            print("{}. {} by {} {} pages".format(count, book[0], book[1], book[2]))
            total_no_pages += int(book[2])
            flag += 1
        count += 1
    print("Total number of pages for {} books: {}".format(flag, total_no_pages))


def list_completed_books(book_list):
    """
    Lists out the books which are marked as completed
    :param book_list: The book list
    :return: The list of Completed books
    """
    total_no_pages = 0
    flag = 0
    count = 0
    print("Completed books:")
    for book in book_list:
        if book[3] == 'c':
            print("{}. {} by {} {} pages".format(count, book[0], book[1], book[2]))
            total_no_pages += int(book[2])
            flag += 1
        count += 1
    print("Total number of pages for {} books: {}".format(flag, total_no_pages))


def add_new_book():
    """
    Adds a new book to the file.
    :return: The new book list
    """
    book_title = str(input(" Please enter the book Title :"))
    while book_title == "":
        print("Input can not be blank")
        print(book_title)
    book_author = str(input(" Please enter the book Author :"))
    while book_author == "":
        print("Input can not be blank")
        print(book_author)
    # bookNumPages = input("Please enter the number of Pages:")
    print()
    flag = 0
    pages = 0
    while flag == 0:
        try:
            pages = int(input("Pages: "))
            while pages <= 0:
                print("Number must be >= 0")
                pages = int(input("Pages: "))
            flag = 1
        except ValueError:
            print("Invalid input; enter a valid number")
    print("{} by {}, ({} pages) added to reading list".format(book_title, book_author, pages))
    book = [book_title, book_author, str(pages), 'r']
    book_list = []
    load_books(book_list)
    book_list.append(book)
    filebook = open(BOOK_FILE, 'w')  # Saving updated data to the file
    for book in book_list:
        print(",".join(book), file=filebook)
    print(file=filebook)
    filebook.close()
    return book_list


def mark_book_completed(book_list): # mark book function declaration
    """
    :param book_list: The book list
    :return: The new book list marked as completed
    """
    list_required_books(book_list)
    print("Enter the number of a book to mark as completed")
    try:
        num_of_book = int(input(">>>"))
        if book_list[num_of_book][3] == 'c':
            print("That book is already completed")
        else:
            book_list[num_of_book][3] = 'c'
            filebook = open(BOOK_FILE, 'w')
            for book in book_list:
                print(",".join(book), file=filebook)
            print(file=filebook)
            filebook.close()
            print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
    except ValueError or IndexError:
        print("Invalid input; enter a valid number")
        mark_book_completed(book_list)


# end of mark book function
main()