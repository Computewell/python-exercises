"""
Write a printASCIITable() function that displays the ASCII number and its corresponding text character,
from 32 to 126.(These are called the printable ASCII characters.)
use the ord() and chr() functions to translate between integers and text characters.
"""

def printASCIITable():
    for i in range(32, 127):
        print(f"{i}--> {chr(i)}")
printASCIITable()