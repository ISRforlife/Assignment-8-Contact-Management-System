
# Contact Management System - Hash Table Assignment

# This class stores a contact's name and phone number
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


# Node class used for handling collisions
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table for storing and searching contacts
class HashTable:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size must be greater than zero")

        self.size = size
        self.data = [None] * size

    # Calculates the index based on the contact's name
    def hash_function(self, key):
        total = 0

        for letter in key:
            total += ord(letter)

        return total % self.size

    # Adds a contact to the table
    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]

        # Check if the contact already exists
        while current is not None:
            if current.key == key:
                current.value.number = value
                return

            current = current.next

        # Create a new contact
        contact = Contact(key, value)
        new_node = Node(key, contact)

        # Add the new node to the linked list
        new_node.next = self.data[index]
        self.data[index] = new_node

    # Searches for a contact by name
    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current is not None:
            if current.key == key:
                return current.value

            current = current.next

        return None

    # Displays all contacts in the hash table
    def print_table(self):
        for i in range(self.size):
            current = self.data[i]

            if current is None:
                print(f"Index {i}: Empty")
            else:
                contacts = []

                while current is not None:
                    contacts.append(str(current.value))
                    current = current.next

                print(f"Index {i}: " + " - ".join(contacts))


# Testing the hash table
if __name__ == "__main__":

    # Create a hash table with 10 spaces
    table = HashTable(10)

    print("Empty Hash Table:")
    table.print_table()

    # Add contacts
    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")

    print("\nAfter Adding Contacts:")
    table.print_table()

    # Search for John
    print("\nSearching for John:")
    print(table.search("John"))

    # Test collisions with Amy and May
    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")

    print("\nAfter Adding Amy and May:")
    table.print_table()

    # Test updating an existing contact
    table.insert("Rebecca", "999-444-9999")

    print("\nAfter Updating Rebecca:")
    table.print_table()

    # Search for a contact that does not exist
    print("\nSearching for Chris:")
    print(table.search("Chris"))
