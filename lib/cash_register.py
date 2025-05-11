#!/usr/bin/env python3

import re

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, item_name, price, quantity=1):
        """
        Adds an item (or multiple of the same item) to the register.
        """
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        for _ in range(quantity):
            self.items.append(item_name)

    def apply_discount(self):
        """
        Applies the store discount to the total and prints a message.
        """
        if self.discount > 0:
            discount_amount = self.total * self.discount / 100
            self.total -= discount_amount
            self.total = int(self.total)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """
        Removes the last transaction amount from the total.
        """
        self.total -= self.last_transaction
        self.last_transaction = 0
