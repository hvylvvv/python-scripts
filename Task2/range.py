'''
Python Script that when given a list of integers, removes duplicates from the list and create a tuple
& finds the minimum and maximum number.
'''
#!/usr/bin/env python3

import argparse

def sortlst(numbers):
    if not numbers:
        raise ValueError("Empty List")
    
    unique_numbers = list(set(numbers))
    number_tuple = tuple(unique_numbers)
    min_num = min(unique_numbers)
    max_num = max(unique_numbers)
    return number_tuple, min_num, max_num

parser = argparse.ArgumentParser(description="Returns a range of numbers of a tuple and the largest and smallest numbers.")
parser.add_argument("numbers", type=int, nargs="+", help="List of positive integers separated by spaces")

args = parser.parse_args()

try:
    numbers = sortlst(args.numbers)
    number_tuple, min_num, max_num = numbers
    print(f"Unique numbers: {number_tuple}")
    print(f"Minimum: {min_num}, Maximum: {max_num}")
except ValueError as e:
    print(e)





# numbers = [int(x) for x in input("Enter a list of integers separated by spaces: ").split()]
# unique_numbers = list(set(numbers))
# number_tuple = tuple(unique_numbers)
# min_num = min(unique_numbers)
# max_num = max(unique_numbers)
# print(f"Unique numbers: {number_tuple}")
# print(f"Minimum: {min_num}, Maximum: {max_num}")
