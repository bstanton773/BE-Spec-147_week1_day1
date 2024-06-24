class Person:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

    # The __str__ method is called any time the object is converted to a string (like print) - end user friendly
    def __str__(self):
        return self.first_name + ' ' + self.last_name

    # The __repr__ method is called by the repr() - developer friendly
    def __repr__(self):
        return f"<Person|{self.first_name} {self.last_name}>"


p1 = Person('Brian', 'Stanton')
p2 = Person('Ryan', 'Rhoades')
p3 = Person('Alex', 'Swiggum')


print(p1)
print(p2)
print(p3)

people = [p1, p2, p3]

print(people)




class Post:
    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    def __str__(self):
        return f"""
{self.title} by {self.author}
{self.body}
"""
    
    def __repr__(self):
        return f"<Post|{self.title}>"
    

post1 = Post('Happy Monday', 'Today is the first day of the back end spec class!', 'Brian')
post2 = Post('Summer', 'The summer solstice happened on Friday. Days are getting shorter!', 'Ryan')

blog = [post1, post2]


print(post1)
print(post2)

print(blog)
