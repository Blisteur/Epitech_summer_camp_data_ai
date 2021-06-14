#!/usr/bin/env python3

from collections import defaultdict
import sys
import json
import os

class budget:
    _balance = 0
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
        for i in self._transactions.values():
            self._balance += i[0]
    def get_category(self):
        return (self._transactions.keys())
    def add_transactions(self, add, cat):
        self._transactions[cat].append(add)
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

def balance(wallet):
    os.system('clear')
    wallet._balance = 0
    for i in wallet._transactions.values():
        for k in i:
            wallet._balance += k
    print("\nYour balance is", wallet._balance, "euros\n")

def add_transaction(wallet):
    os.system('clear')
    stop = True
    len_category = len(wallet._transactions.keys())
    while stop:
        print("Adding transaction:")
        if (len_category > 0):
            print("You have actually", len_category, "category:")
            nb = 1
            for i in wallet._transactions.keys():
                print(nb, i)
                nb += 1
        try:
            category = input("choose category or add a new: ")
        except EOFError:
            break
        try:
            euros = input("transaction number: ")
        except EOFError:
            break
        wallet.add_transactions(int(euros), category)
        stop = False
    os.system('clear')

def history(wallet):
    os.system('clear')
    print("Your transaction history:")
    print("\n--------------------------------\n")
    for category in wallet.get_category():
        print(category)
        wallet.show_transactions(category)
    print("\n--------------------------------\n")

def menu(wallet):
    stop = True
    while stop:
        print("Choose between :")
        print("1 - consult my balance")
        print("2 - add a new transaction")
        print("3 - consult your transactions history")
        print("4 - quit")
        try:
            cmd = input()
            if (cmd == "1"):
                balance(wallet)
            if (cmd == "2"):
                add_transaction(wallet)
            if (cmd == "3"):
                history(wallet)
            if (cmd == "4"):
                stop = False
        except EOFError:
            break

#def save(wallet):
#    save_file = "{\n\t\"transactions\" : [\n"
#    for i in wallet._transactions:

def main(argv):
    wallet = budget("./data.json")
    menu(wallet)
    #save(wallet)

main(sys.argv)