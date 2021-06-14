#!/usr/bin/env python3

import sys

class budget:
    _transactions = []
    def add_transactions(self, add):
        self._transactions.extend(add)
    def show_transactions(self):
        for i in self._transactions:
            if (i > 0):
                print("You received", i ,"euros")
            if (i < 0):
                print("You spent", i * -1 ,"euros")

def main(argv):
    transactions = [512, 42.08, -12]
    wallet = budget()
    wallet.add_transactions(transactions)
    wallet.show_transactions()

main(sys.argv)