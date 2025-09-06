import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from skiplist import SkipList  # Import your SkipList implementation

class GroceryTransactionManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grocery Transaction Manager")
        self.skip_list = SkipList(4, 0.5)  # Create a SkipList instance
        self.init_ui()

    def init_ui(self):
        # Create input fields
        self.key_input = QLineEdit()
        self.value_input = QLineEdit()

        # Create buttons
        self.add_button = QPushButton("Add Transaction")
        self.search_button = QPushButton("Search Transaction")
        self.delete_button = QPushButton("Delete Transaction")

        # Create labels for input fields
        key_label = QLabel("Transaction Key:")
        value_label = QLabel("Transaction Value:")

        # Connect buttons to event handlers
        self.add_button.clicked.connect(self.add_transaction)
        self.search_button.clicked.connect(self.search_transaction)
        self.delete_button.clicked.connect(self.delete_transaction)

        # Layout setup
        input_layout = QVBoxLayout()
        input_layout.addWidget(key_label)
        input_layout.addWidget(self.key_input)
        input_layout.addWidget(value_label)
        input_layout.addWidget(self.value_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.search_button)
        button_layout.addWidget(self.delete_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def add_transaction(self):
        key = int(self.key_input.text())
        value = self.value_input.text()
        self.skip_list.insert(key, value)
        self.key_input.clear()
        self.value_input.clear()
        self.display_skip_list()

    def search_transaction(self):
        key = int(self.key_input.text())
        result = self.skip_list.search(key)
        if result:
            print("Transaction found:", result)
            # Display or handle the result as needed
        else:
            print("Transaction not found")

    def delete_transaction(self):
        key = int(self.key_input.text())
        self.skip_list.delete(key)
        self.display_skip_list()

    def display_skip_list(self):
        print("\nSkip List:")
        self.skip_list.display()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GroceryTransactionManager()
    window.show()
    sys.exit(app.exec_())
