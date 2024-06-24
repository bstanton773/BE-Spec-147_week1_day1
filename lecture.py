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