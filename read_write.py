""" 
Write a writeToFile() function with two parameters for the filename of the file 
and the text to write into the file. Second, write an appendToFile() function,
which is identical to writeToFile() except that the file opens in append mode instead of write mode. 
Finally, write a readFromFile() function with one parameter for the filename to open.
This function returns the full text contents of the file as a string 
"""

def writeToFile(filename, text):
    with open(filename, "w") as file:
        file.write(text)
        
def appendToFile(filename, text):
    with open(filename, "a") as file:
        file.write(text)
        
def readFromFile(filename):
    with open(filename, "r") as file:
        return file.read()