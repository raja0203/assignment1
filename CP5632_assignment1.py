"""
NAME : RAJA VIGNESH VIRKUDI RAGHUNATH
DATE : 06/01/2017
PROGRAM DETAILS : This program is a simple reading list where we create an empty list BOOK_LIST and perform read , write operations to the CSV file /
                 Along with, two more operations Add and mark book functions. Program functions as per the users input and performs operations based
                 on the required User inputs.
GITHUB LINK     :   https://github.com/raja0203/assignment1.git
"""
__author__ = "Raja Vignesh Virkudi Raghunath"


# Initialize the constants
BOOK_FILE = "books.csv"

def main():
        print('Reading List 1.0 - by Raja Vignesh Virkudi Raghunath')

        # load books from the file

        book_list = []
        load_books(book_list)
#print(book_list)
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



# end of main()

def display_menu():
    # print the menu
    print("menu:")
    print("R - List required books")
    print("C - List completed books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
    print()


def load_books(book_list):  # loading books from file to list

    file = open(BOOK_FILE,'r')
    for line in file:
        book_list.append(line.strip().split(','))

# end of load_books()
def list_required_books(book_list): # Required books function declaration
    total_no_pages = 0
    flag =0
    count = 0
    print("Required books:")
    for i in book_list:
        if 'r' in book_list [count][3]:
            print("{}. {} by {} {} pages".format(count, book_list[count][0],book_list[count][1],book_list[count][2]))
            total_no_pages =total_no_pages+int(book_list[count][2])
            flag+=1
        count=count+1
    print("Total number of pages for {} books: {}".format(flag,total_no_pages))

def list_completed_books(book_list): # Completed books function declaration
    total_no_pages = 0
    flag = 0
    count = 0
    print("Required books:")
    for i in book_list:
        if 'c' in book_list[count][3]:
            print("{} by {} {} pages".format(book_list[count][0], book_list[count][1], book_list[count][2]))
            total_no_pages = total_no_pages + int(book_list[count][2])
            flag += 1
        count = count + 1
    print("Total number of pages for {} books: {}".format(flag , total_no_pages))


def add_new_book(): # add news books function declaration
    bookTitle = str(input(" Please enter the book Title :"))
    while bookTitle == "":
            print("Input can not be blank")
            print(bookTitle)
    bookAuthor = str(input(" Please enter the book Author :"))
    while bookAuthor == "":
            print("Input can not be blank")
            print(bookAuthor)
#bookNumPages = input("Please enter the book Pages number:")
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
    print("{} by {}, ({} pages) added to reading list".format(bookTitle, bookAuthor, pages))
    book = [bookTitle, bookAuthor, str(pages), 'r']
    book_list = []
    load_books(book_list)
    book_list.append(book)
    filebook = open(BOOK_FILE, 'w') #Saving updated data to the file
    for i in book_list:
        for j in i:
            if j == "r" or j == "c":
                print(j, end='', file=filebook)
            else:
                print(j, end=',', file=filebook)
        print(file=filebook)
    filebook.close()
    return book_list
#new_book = str(bookTi1tle + "," + bookAuthor + "," + bookNumPages)


def mark_book_completed(book_list): # mark book function declaration
    list_required_books(book_list)
    print("Enter the number of a book to mark as completed")
    try:
        num_of_book = int(input(">>>"))
        if book_list[num_of_book][3] == 'c':
            print("That book is already completed")
        else:
            book_list[num_of_book][3] = 'c'
            filebook = open(BOOK_FILE, 'w')
            for i in book_list:
                for j in i:
                    if j == "r" or j == "c":
                        print(j, end='', file=filebook)
                    else:
                        print(j, end=',', file=filebook)
                print(file=filebook)
            filebook.close()
            print("{} by {} is completed".format(book_list[num_of_book][0], book_list[num_of_book][1]))
    except ValueError:
        print("Invalid input; enter a valid number")
        mark_book_completed(book_list)
#end of mark book function
main()

