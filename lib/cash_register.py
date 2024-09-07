#!/usr/bin/env python3


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity
        self.total += price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        if self.items:
            last_item = self.items[-1]
            count_to_remove = self.items.count(last_item)
            for _ in range(count_to_remove):
                self.items.pop()
        self.last_transaction = 0


cash_register_with_discount = CashRegister(1000)
cash_register_with_discount.apply_discount()
