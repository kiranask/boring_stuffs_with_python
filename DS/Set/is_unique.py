# Check if String has unique character
"""
Implement an algorithm to determine if a string has all unique characters.
"""

def is_unique(given_string):
    return len(given_string) == len(set(given_string))
print(is_unique("KiranSK"))

