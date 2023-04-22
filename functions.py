# Create a list of Person objects called people with at least three elements
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("John", 25),
    Person("Jane", 32),
    Person("Bob", 40)
]
print(people)

# Print out the name of the second person in the list.
print (people[1])