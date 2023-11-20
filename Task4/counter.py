'''
Python script that when given an input string, 
count occurrences of all characters within a string 
(e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2).
'''

#!/usr/bin/env python3

import argparse

def charcounter(inputstr):
    #str = input("Enter a string: ")
    count = {}
    # for char in inputstr:
    #     if char in count:
    #         count[char] += 1
    #     else:
    #         count[char] = 1
   
    # for char, count in count.items():
    #     print(f"{char}:{count}", end=", ")
    # print()

    count = {char: inputstr.count(char) for char in set(inputstr)}

    for char, count in count.items():
        print(f"{char}:{count}", end=", ")
    print()


parser = argparse.ArgumentParser(description="Returns the total number of characters in a given string")
parser.add_argument("string",  help="Input string value with characters to be counted.")

args = parser.parse_args()

try:
    charcounter(args.string)
except ValueError as e:
    print(e)
