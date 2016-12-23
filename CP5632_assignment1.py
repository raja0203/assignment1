__author__ = "Raja Vignesh Virkudi Raghunath"

# Initialize the constants
BOOK_FILE = "books.csv"

def main():
    print('Reading List 1.0 - by Raja Vignesh Virkudi Raghunath')

    #load books from the file

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
            add_new_book(book_list)
        elif choice == 'M':
            mark_book_completed(book_list)
        else:
            print('Please enter R, C, A, M or Q(uit) ')
        display_menu()
        choice = input('>>>').upper()
    print('Have a nice day :) ')
#end of main()

def display_menu ():
    #print the menu
    print("menu:")
    print("R - List required books")
    print("C - List completed books")
    print("A - Add new book")
    print("M - Mark a book as completed")
    print("Q - Quit")
def load_books(book_list): #using for loop in week 2
    """

    """
    print("load books")

# end of load_books()
def list_required_books(book_list):
    print('list_required_books')
def list_completed_books(book_list):
    print('list_completed_books')
def add_new_book(book_list):
    print('add_new_book')
def mark_book_completed(book_list):
    print('mark_book_completed')
    """

    """
    print("complete a book")

# end of complete_a_book()

# Start the program
main()