'''
2. Python Data Structure Challenges in Real-World Scenarios

Objective:

This assignment is designed to enhance your understanding and application of Python's core data structures - tuples, lists, and dictionaries
- in real-world contexts. 
By engaging with these tasks, you will practice manipulating these data structures, applying built-in Python methods, 
and implementing error handling in practical situations.

Task 1: Library System Enhancement
Sharpen your skills in managing and modifying data within tuples and lists.

Problem Statement:
You are maintaining a library system where each book is stored as a tuple within a list. 
Your task is to update this system by adding new books and ensuring no duplicates.

Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

Add functionality to insert new books into library.
Ensure that adding a duplicate book is handled appropriately.
'''

def add_book(catalog):
    input_title = input("\nPlease enter the title of your book ")
    input_author = input("Please enter the name of the author ")
    lib = (input_title, input_author)

    if lib in catalog:
        print("This information already exists")
    else:
        catalog.add(lib)
        print("Book added successfully")



def display_books(catalog):
    for title, author in catalog:
        print(f"\nTitle: {title} - Author: {author}")


library = set()

while True:
    print("\n1. Add book")
    print("2. Display books")
    print("3. Quit")
    input_user = int(input("Which would you like to choose? "))

    if input_user == 1:
        add_book(library)
    elif input_user == 2:
        display_books(library)
    elif input_user == 3:
        break
    else:
        print("Please look over the options and provide the number of your chouce!")
