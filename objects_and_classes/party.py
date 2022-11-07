# Create a class Party that only has an attribute people – empty list.
# The __init__ method should not accept any parameters.
# You will be given names of people (on separate lines) until you receive the command "End".
# Use the created class to solve this problem. After you receive the "End" command, print 2 lines:
# •	"Going: {people}" - the people should be separated by comma and space ", ".
# •	"Total: {total_people_going}"
# Note: submit all of your code, including the class


class Guest:
    def __init__(self, name):
        self.name = name


class Party:
    def __init__(self):
        self.people = []

    def invite(self, person):
        self.people.append(person)

    def names_of_the_people(self):
        return ', '.join([person.name for person in self.people])

    def number_of_guests(self):
        return len(self.people)


party = Party()

while True:

    command = input()

    if command == "End":
        break

    name = command
    guest = Guest(name)
    party.invite(guest)

print(f"Going: {party.names_of_the_people()}")
print(f"Total: {party.number_of_guests()}")