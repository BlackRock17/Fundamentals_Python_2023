class Party:

    def __init__(self):
        self.people = []

    def total(self):
        return len(self.people)

    def names(self):
        return ', '.join(person for person in self.people)

party = Party()

while True:
    name = input()

    if name == "End":
        break

    party.people.append(name)

print(f"Going: {party.names()}")
print(f"Total: {party.total()}")
