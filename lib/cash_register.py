#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0.0
        self.items = []
        self.last_transaction_total = 0.0
        self.last_transaction_items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction_total = price * quantity
        self.last_transaction_items = [title] * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total = round(self.total - discount_amount, 2)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction_total
        self.total = round(self.total, 2)
        # Remove last transaction items from items list
        for item in self.last_transaction_items:
            if item in self.items:
                self.items.remove(item)
        # Reset last transaction info
        self.last_transaction_total = 0.0
        self.last_transaction_items = []
