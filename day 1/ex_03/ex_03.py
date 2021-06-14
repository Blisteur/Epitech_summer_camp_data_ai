#!/usr/bin/env python3

from collections import defaultdict
import sys
import json

class budget:
    _transactions = defaultdict(list)
    def __init__(self, filename=None):
        if (filename == None):
            return
        file = open(filename)
        data = json.load(file)
        for i in data['transactions']:
            if (i['category'] not in self._transactions.keys()):
                self._transactions[i['category']] = [i['value']]
            else:
                self._transactions[i['category']].append(i['value'])
        file.close()
    def get_category(self):
        return (self._transactions.keys())
    def add_transactions(self, add, cat):
        self._transactions[cat].extend(add)
    def show_transactions(self, cat):
        for i in self._transactions[cat]:
            try:
                if (i > 0):
                    print("You received", i ,"euros")
                if (i < 0):
                    print("You spent", i * -1 ,"euros")
            except TypeError:
                print("Invalide type \"", i, "\"")
                break

def main(argv):
    transactions = [512, 42.08, -12]
    wallet = budget("./data.json")
    for category in wallet.get_category():
        print(category)
        wallet.show_transactions(category)

main(sys.argv)