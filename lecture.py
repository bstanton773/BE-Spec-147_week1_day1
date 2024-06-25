import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)


##############################################
# Data Structures and Algorithm Fundamentals #
##############################################


# Lists
# Ordered collection of items, allowing for sequential storage and retrieval

fiction_books = ['Dune', '1984', 'Brave New World', 'Neuromancer']
print(fiction_books)
print(type(fiction_books))


line_break()

# Dictionaries
# unordered key-value pairs, providing fast and flexible way to retrieve information
# As of Python 3.6, Dictionaries will remember the order in which key-value pairs were added

book_locations = {
    'Dune': 'Fiction Section, Shelf 2',
    '1984': 'Fiction Section, Shelf 4',
    'Brave New World': 'Fiction Section, Shelf 1',
    'Neuromancer': 'Fiction Section, Shelf 3'
}

print(book_locations)
print(type(book_locations))


line_break()


# Linked List
# Linear Data Structure where each element (node) points to the next one, allows for dynamic and efficient insertion or removal

# Create a Node Class for each element that will have two attributs:
# .value that will be the value of the node, and then a .next that will point to the next node in the Linked List

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<Node|{self.value}>"


# Create a Linked List Class (data structure) that has one attribute: .head will point to the first Node in the Linked List
# And has one method: traverse which will print each node in the list

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        # Start at the head node
        current_node = self.head
        # While the current node is a Node
        while current_node is not None:
            # print the current node
            print(current_node)
            # Set the current node to the next node in the list
            current_node = current_node.next


library_books = LinkedList()
library_books.head = Node('Dune')
library_books.head.next = Node('1984')
library_books.head.next.next = Node('Brave New World')
library_books.head.next.next.next = Node('Neuromancer')

library_books.traverse()

line_break()


# Stacks
# Follow the Last In First Out (LIFO) principle
# think of a stack of pancakes - the most recent pancake made will be the first one eaten

from collections import deque

browser_history = deque()
browser_history.append('codingtemple.com')
browser_history.append('pythontutor.com')
browser_history.append('w3schools.com')
browser_history.append('docs.python.org')

print(browser_history)

while browser_history:
    current_page = browser_history.pop()
    print('Currently on:', current_page)
    print('Clicking the back button...\n')

print(browser_history)


line_break()

# Queues
# Follow the First In First Out (FIFO) principle
# Think of waiting in line for the hottest ticket in town - the first person in line will be the first person to get tickets

cashier_line = deque()
cashier_line.append('Alice')
cashier_line.append('Bob')
cashier_line.append('Catherine')
cashier_line.append('David')

print(cashier_line)

while cashier_line:
    current_customer = cashier_line.popleft()
    print('Currently ringing up:', current_customer)
    print('"Next!"\n')

print(cashier_line)


cashier_line = []
cashier_line.append('Alice')
cashier_line.append('Bob')
cashier_line.append('Catherine')
cashier_line.append('David')

print(cashier_line)

while cashier_line:
    current_customer = cashier_line.pop(0)
    print('Currently ringing up:', current_customer)
    print('"Next!"\n')

print(cashier_line)


line_break()

# Binary Tree
# Heirarchical structure where each node has at most two children (.left and .right)
# Each Node is a Binary Tree itself


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"<BinaryTree|{self.value}"


root = BinaryTree(50)
root.left = BinaryTree(25)
root.right = BinaryTree(75)
root.left.left = BinaryTree(10)
root.left.right = BinaryTree(45)
root.right.left = BinaryTree(60)
root.right.right = BinaryTree(90)


line_break()

# Graphs 
# consists of nodes and edges, represent relationships between entities

#      Erika
#     /     \
#    /       \
# Felix --- Grace
#    \       /
#     \     /
#      Henry

friend_graph = {
    "Erika": ["Felix", "Grace"],
    "Felix": ["Erika", "Grace", "Henry"],
    "Grace": ["Erika", "Felix", "Henry"],
    "Henry": ["Felix", "Grace"]
}

for person, friends in friend_graph.items():
    print(f"{person} is friends with {', '.join(friends)}")



line_break()
line_break()

#############################
# Data Structure Operations #
#############################

print(fiction_books)

# Sorting Algorithm
# 2 main ways to sort a list - builtin sorted() and list method .sort()
# sorted - out of place - a new sorted list is created from the original. Original is unchanged
# .sort - in place - the original list is sorted

print('Before sorted:', fiction_books)
sorted_books = sorted(fiction_books)
print('After sorted:', fiction_books) # This will be the same as before the sorted function
print('Sorted return:', sorted_books) # will return the NEW sorted list


print('Before .sort:', fiction_books)
sorted_books2 = fiction_books.sort()
print('After .sort:', fiction_books) # This will be different as it was before the .sort method
print('Sort return:', sorted_books2) # will return None, the original list has been modified


# Searching Algorithm
# Searching function take on the role of detective, looking for specific data
# use the 'in' keyword

# desired_book = input("Please enter a book title: ").title()
desired_book = "Dune"
print('Searching...')
if desired_book in fiction_books: # Linear Search of the list - sequentially check each element 
    print(f"{desired_book} is in the Fiction Section")
else:
    print(f"{desired_book} is NOT in the library")


# Inserting into a list
# Insertion functions add elements while maintaining the structural integrity

print('Inserting...')
new_book = "The Great Gatsby"
fiction_books.append(new_book) # Will add to the end of the list
print(fiction_books)


print('Inserting...')
new_book2 = "The Catcher in the Rye"
fiction_books.insert(2, new_book2) # Will insert at a specific index, shift all elements after one index up
print(fiction_books)


# Deletion Algorithm
# Deletion functions remove elements while maintaining the structural integrity

print('Deleting...')
fiction_books.pop() # Will remove the last element from the list
print(fiction_books)


print('Deleting...')
unwanted_book = 'Brave New World'
fiction_books.remove(unwanted_book)
print(fiction_books)


line_break()

# Dictionaries
# Searching, Inserting and Deleting

addresses = {
    'Brian': '123 Real Street',
    'Ryan': '321 Fake Street',
    'Alex': '555 Circle Drive'
}


# Searching - also uses the 'in' keyword
print('Searching...')
# lookup = input('Please enter a name: ')
lookup = 'Brian'
if lookup in addresses: # 'in' with dictionary will check for key - constant time lookup
    print(f"{lookup} lives at {addresses[lookup]}")
else:
    print(f"{lookup} is not in the address book")


# Inserting
# dict[key] = value

print('Inserting...')
addresses['Kevin'] = '444 Square Rd'
print(addresses)


# Deleting
print('Deleting...')
addresses.pop('Alex') # Key that we want to remove, value will be removed as well

print(addresses)

line_break()
line_break()

print('''
You have been tasked with developing a library cataloging system for a local library. The system should allow librarians to efficiently
manage and retrieve books from different sections of the library.

Your task is to implement a Python class called Library that provides the following functionalities:

Adding Books: 
    The add_book method should take two parameters: section (a string indicating the section of the library where the book belongs) and book (a string indicating the title of the book). If the specified section already exists in the library, the book should be added to that section. If the section does not exist, it should be created, and the book should be added to it.

Retrieving Books: 
    The retrieve_books method should take one parameter: section (a string indicating the section of the library from which books should be retrieved). It should return all of the books in the specified section. If the section does not exist or if there are no books in the section, it should return the string "No books available in this section."
''')


class Library:
    def __init__(self):
        self.sections = {
            "Health": []
        }

    def add_book(self, section, book):
        # Check if the section argument is a key in the sections dictionary
        if section in self.sections:
            # Add the book to that section
            self.sections[section].append(book)
        # If the section argument is not in the dictionary
        else:
            # Create the section and add the book to the section
            self.sections[section] = [book]

    def retrieve_books(self, section):
        # Check if the section exists  and that there are books in that section
        if section in self.sections and self.sections[section]:
            # Return all of the books in that section
            return self.sections[section]
        # If the section does not exist
        else:
            # Return no books avail
            return 'No books available in this section'

# Example usage:
library = Library()

# Adding books to the library
library.add_book("Fiction", "1984")
library.add_book("Fiction", "Brave New World")
library.add_book("Non-Fiction", "Freakonomics")

# Retrieving books from the library
print(library.retrieve_books("Fiction"))  # Output: ["1984", "Brave New World"]
print(library.retrieve_books("Non-Fiction"))  # Output: ["Freakonomics"]
print(library.retrieve_books("Science"))  # Output: "No books available in this section."
print(library.retrieve_books("Health"))  # Output: "No books available in this section."


#############################
# Time and Space Complexity #
#############################

# Big O notation is a mathematical notation used in computer science to describe the performance or complexity of an 
# algorithm. It provides a way to express the upper bound of the time or space required by an algorithm as a function 
# of the size of the input.

# Time complexity refers to the amount of time an algorithm takes to complete as a function of the size of its input. 
# It's typically expressed using Big O notation and describes how the runtime of an algorithm grows as the input size increases.

# Space complexity, on the other hand, refers to the amount of memory space an algorithm requires as a function 
# of the size of its input. Like time complexity, it's also expressed using Big O notation and describes how the 
# memory usage of an algorithm grows as the input size increases.

# Understanding time and space complexity helps developers analyze and compare different algorithms to determine which 
# ones are more efficient for solving specific problems. It's a crucial concept in algorithm design and optimization.

# Complexities - Best to Worst
# O(1) - Constant
# O(log n) - logarithmic
# O(n) - linear
# O(n log n) - linear logarithmic
# O(n**2) - quadratic


# Step 1: Create a really big list
big_list = [f"stone_{i}" for i in range(1, 100001)]

# Step 2: Measure the time it takes to find the last stone (stone_100000)
import time

start = time.time()
print('stone_100000' in big_list)
end = time.time()

print(f"It took {end - start} seconds to find stone_100000")


# Step 3: Create a similar sized dictionary
big_dict = {'stone_'+ str(i): 'rock' for i in range(1,100001)}

# Step 4: Measure the time it takes to find the key "stone_100000"

start = time.time()
print('stone_100000' in big_dict)
end = time.time()

print(f"It took {end - start} seconds to find stone_100000")


line_break()
line_break()


contacts = [
    ("Alice", "555-1234"),
    ("Bob", "555-5678"),
    ("Charlie", "555-9012"),
    ("David", "555-3456"),
    ("Emma", "555-7890"),
    ("Frank", "555-2345"),
    ("Grace", "555-6789"),
    ("Henry", "555-0123"),
    ("Ivy", "555-4567"),
    ("Jack", "555-8901"),
    ("Kate", "555-3456"),
    ("Liam", "555-7890"),
    ("Mia", "555-2345"),
    ("Noah", "555-6789"),
    ("Olivia", "555-0123"),
    ("Peter", "555-4567"),
    ("Quinn", "555-8901"),
    ("Rachel", "555-2345"),
    ("Sam", "555-6789"),
    ("Taylor", "555-0123"),
    ("Uma", "555-4567"),
    ("Victor", "555-8901"),
    ("Wendy", "555-2345"),
    ("Xavier", "555-6789"),
    ("Yara", "555-0123"),
    ("Zoe", "555-4567"),
    ("Grace", "555-6789"),
    ("Henry", "555-0123"),
    ("Ivy", "555-4567"),
    ("Jack", "555-8901"),
    ("Kate", "555-3456"),
    ("Liam", "555-7890"),
    ("Mia", "555-2345"),
    ("Noah", "555-6789"),
    ("Olivia", "555-0123"),
    ("Peter", "555-4567"),
    ("Quinn", "555-8901"),
    ("Rachel", "555-2345"),
    ("Sam", "555-6789"),
    ("Taylor", "555-0123"),
    ("Uma", "555-4567"),
    ("Victor", "555-8901"),
    ("Wendy", "555-2345"),
    ("Xavier", "555-6789"),
    ("Yara", "555-0123"),
    ("Zoe", "555-4567")
]

my_people = [("Victor", "555-5555"), ("Chris", "444-4444")]


def get_phone_number(address_book, target_name):
    num_checks = 0
    # Loop through each tuple in the address book - unpack tuple - 0-index is name, 1-index is number
    for name, number in address_book:
        num_checks += 1
        # Compare the name to the target name
        if name == target_name:
            # Return the associated number
            print(f'It took {num_checks}')
            return number
    # If we loop through all of the contacts without returning, we know target is not in the book
    print(f'It took {num_checks}')
    return -1


# Best Case - O(1) - Constant Time
print(get_phone_number(contacts, 'Alice'))

# Worst Case - O(n) - Linear Time
print(get_phone_number(contacts, "Victor"))


def find_all(address_book, target_name):
    output = []
    num_checks = 0
    # Loop through each tuple in the address book - unpack tuple - 0-index is name, 1-index is number
    for name, number in address_book:
        num_checks += 1
        # Compare the name to the target name
        if name == target_name:
            output.append(number)
    print(f'It took {num_checks}')
    return output if output else -1

# Best Case - O(n) - Linear Time
print(find_all(contacts, 'Alice'))

# Worst Case - O(n) - Linear Time
print(find_all(contacts, "Victor"))


line_break()

# Time and Space Complexities
fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'watermelon', 'strawberry']


# Indexing a List
# Constant Time and Space - O(1)
indexing = fruits[3]
print(indexing)


# Searching Through a List
# Linear Time - O(n) and Constant Space - O(1)
print('watermelon' in fruits)
print('mango' in fruits)


# Copying a list 
# Linear Time - O(n) and Linear Space - O(n)
copied_fruits = fruits[:]
print(copied_fruits)


# Assigning a value to a list index
# Constant Time - O(1) and Constant Space - O(1)
fruits[3] = 'grapefruit'
print(fruits)


# Insertion - list.append
# Constant Time - O(1) and Constant Space - O(1)
fruits.append('mango')
print(fruits)


# Insertion - list.insert
# Linear Time - O(n) and Constant Space - O(1)
fruits.insert(0, 'pear')
print(fruits)


# Deletion - list.pop - default -1 or any negative index
# Constant Time - O(1) and Constant Space - O(1)
last_element = fruits.pop()
print(fruits)
print(last_element)

# Deletion - list.pop - any non-negative index
# Linear Time - O(n) and Constant Space - O(1)
first_element = fruits.pop(0)
print(fruits)
print(first_element)


# Sorting - sorted() = Python sorted also uses the timsort
# Linear Logarithmic Time - O(n log n) and Linear Space - O(n)
sorted_fruits = sorted(fruits)
print(sorted_fruits)
print(fruits)


# Sorting - list.sort - Python list uses timsort sorting algorithm
# Linear Logarithmic - O(n log n) and Constant Space - O(1)
fruits.sort()
print(fruits)



line_break()
# Time and Space Complexities of Python Dictionaries

fruit_counts = {}

# Insertion
# Constant Time and Constant Space - O(1)
fruit_counts['apple'] = 10
fruit_counts['banana'] = 15
fruit_counts['orange'] = 20

print(fruit_counts)


# Accessing
# Constant Time and Constant Space - O(1)
print(fruit_counts['apple'])
print(fruit_counts.get('banana'))
print(fruit_counts.get('strawberry', 'No Strawberries'))


# Searching
# Constant Time and Constant Space - O(1)
print('apple' in fruit_counts)
print('watermelon' in fruit_counts)


# Updating value via a key
# Constant Time and Constant Space - O(1)
fruit_counts['banana'] = 30
print(fruit_counts)


# Removing Key,Value pairs
# Constant Time and Constant Space - O(1)
fruit_counts.pop('orange')
print(fruit_counts)


# Real World Application - Authentication

users = [(f"user{i}", "password{i}") for i in range(100000)]


print('To Log In please enter your credentials')
username = input('Enter username: ')
password = input('Enter password: ')

# for user in users:
#     if user[0] == username and user[1] == password:
#         print('You have successfully logged in')
#         break
# else: # An else after a for loop only runs if the for loop does not break
#     print('Incorrect username/password')
start = time.time()
if (username, password) in users: # Linear Time Search
    print('You have successfully logged in')
else:
    print('Incorrect username/password')
end = time.time()

print(end - start)

# Setup again but with a dictionary
users = {f"user{i}": f"password{i}" for i in range(100000)}

print('To Log In please enter your credentials')
username = input('Enter username: ')
password = input('Enter password: ')

start = time.time()
if username in users and users[username] == password: # Constant Time 
    print('You have successfully logged in')
else:
    print('Incorrect username/password')
end = time.time()


print(end - start)