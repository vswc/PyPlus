"""
User is a class with 'name' and 'age' attributes.
Classes are used to create objects, which store data.

__init__ is a function called when the object is created, and self is a reference to the object.

When adding 'name' and 'age' attributes to a class, they are automatically included in the object. This object is stored in the 'user' variable, representing an instance of the 'User' class. The attributes, 'name' and 'age,' can be accessed using dot notation.
"""

class User:
  # Create a new instance of the class
  def __init__(self, name, age):
    self.name = name
    self.age = age

user = User("vsw", 18)

print(user.name)
    # object.attribute
print(user.age) 
    # object.attribute

"""
Anything I missed? Let me know.
@vsw on discord.
"""