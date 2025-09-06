import random
from PyQt5.QtWidgets import QApplication, QWidget
class Node:
    def __init__(self, key=None, value=None, level=None):
        self.key = key
        self.value = value
        self.forward = [None] * level

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.header = self.create_node(max_level, None, None)

    def create_node(self, level, key, value):
        return Node(key, value, level)

    def random_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, key, value):
        update = [None] * (self.max_level)
        current = self.header

        for i in range(self.max_level - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        level = self.random_level()
        new_node = self.create_node(level, key, value)

        for i in range(level):
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        for i in range(self.max_level - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return current.value
        else:
            return None

    def delete(self, key):
        update = [None] * (self.max_level)
        current = self.header

        for i in range(self.max_level - 1, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]
        if current and current.key == key:
            for i in range(len(current.forward)):
                update[i].forward[i] = current.forward[i]
            del current

    def display(self):
        for level in range(self.max_level - 1, -1, -1):
            current = self.header
            print("Level {}: ".format(level), end=" ")
            while current.forward[level]:
                print(current.forward[level].key, end=" -> ")
                current = current.forward[level]
            print("")


# Example usage:
if __name__ == "__main__":
    # Creating a skip list with max level 4 and probability 0.5
    skip_list = SkipList(4, 0.5)

    # Inserting some transactions
    skip_list.insert(10, "Transaction 1")
    skip_list.insert(20, "Transaction 2")
    skip_list.insert(30, "Transaction 3")
    skip_list.insert(15, "Transaction 4")
    skip_list.insert(25, "Transaction 5")

    # Display the skip list
    print("Skip List:")
    skip_list.display()

    # Searching for a transaction
    print("\nSearching for transaction with key 20:")
    result = skip_list.search(20)
    if result:
        print("Transaction found:", result)
    else:
        print("Transaction not found")

    # Deleting a transaction
    print("\nDeleting transaction with key 20:")
    skip_list.delete(20)

    # Display the skip list after deletion
    print("\nSkip List after deletion:")
    skip_list.display()
