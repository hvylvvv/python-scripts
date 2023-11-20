
'''
Pyhton script that accepts the file name and puts its extension to output. 
If there is no extension - an exception should be raised
'''

#!/usr/bin/env python3

import os

def get_file_extension(file_name):
    if not '.' in file_name:
        raise ValueError("The file has no extension.")
    return os.path.splitext(file_name)[1]

file_name = input("Enter the file name: ")
try:
    extension = get_file_extension(file_name)
    print(f"File extension: {extension}")
except ValueError as e:
    print(e)







