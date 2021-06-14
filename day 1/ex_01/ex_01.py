#!/usr/bin/env python3

import sys

def show_transactions(list):
    for i in list:
        if (i > 0):
            print("You received", i ,"euros")
        if (i < 0):
            print("You spent", i * -1 ,"euros")

def main(argv):
    transactions = [512, 42.08, -12]
    show_transactions(transactions)

main(sys.argv)