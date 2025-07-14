#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initializes the CashRegister.

        Args:
            discount (int, optional): Percentage discount. Defaults to 0.
        """
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction_amount = 0.0

    def add_item(self, name, price, quantity=1):
        """
        Adds an item (or multiple) to the register.

        Args:
            name (str): Item name
            price (float): Price of one unit
            quantity (int, optional): How many to add. Defaults to 1.
        """
        self.total += price * quantity
        self.items.extend([name] * quantity)
        self.last_transaction_amount = price * quantity

    def apply_discount(self):
        """
        Applies the discount to the total, if any.
        Prints a message about the result.
        """
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last added transaction from the total.
        """
        self.total -= self.last_transaction_amount
        self.last_transaction_amount = 0.0
