# Exercise 1 --> Hello, World!
""" Write a program that, when run, greets the user by printing ―Hello, world!‖ on the screen.
Then it prints a message on the screen asking the user to enter their name. The program greets the user by name by printing the ―Hello,followed by the user's name. """

print("Hello, world!")
names = input("What is your name?\n")
print(f"Hello, {names} !")

# Exercise 2 --> Temperature Conversion
""" Write a convertToFahrenheit() function with a degreesCelsius parameter. This function returns the number of this temperature in degrees Fahrenheit. 
Then write a function named convertToCelsius() with a degreesFahrenheit parameter and returns a number of this temperature in degrees Celsius. """

def convert_to_fahrenheit(degrees_celsius):
    return degrees_celsius * (9 / 5) + 32

def convert_to_celsius(degrees_fahrenheit):
    return (degrees_fahrenheit - 32) * 5 / 9

assert convert_to_celsius(0) == -17.77777777777778
assert convert_to_celsius(180) == 82.22222222222223
assert convert_to_fahrenheit(0) == 32
assert convert_to_fahrenheit(100) == 212
assert convert_to_celsius(convert_to_fahrenheit(15)) == 15
# Rounding errors cause a slight discrepancy:
assert convert_to_celsius(convert_to_fahrenheit(42)) == 42.00000000000001

# Exercise 3 --> Odd & Even
""" Write two functions, isOdd() and isEven(), with a single numeric parameter named number.
The isOdd() function returns True if number is odd and False if number is even. The isEven() function returns the True if number is even and False if number is odd.
Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered an even number. """

def isOdd(number):
    return number % 2 == 1

def isEven(number):
    return number % 2 == 0

assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False

# Exercise 4 --> Area & Volume
""" You will write four functions for this exercise. The functions area() and perimeter() have length and width parameters and the functions volume() and surfaceArea() have length,
width, and height parameters. These functions return the area, perimeter, volume, and surface area, respectively """

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

def volume(length, width, height):
    return length * width * height

def surfaceArea(length, width, height):
    return 2 * (length * width + length * height + width * height)

assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340

# Exercise 5 --> Fizz Buzz
""" Write a fizzBuzz() function with a single integer parameter named upTo. For the numbers 1 up to and including upTo, the function prints one of four things:
 Prints 'FizzBuzz' if the number is divisible by 3 and 5.
 Prints 'Fizz' if the number is only divisible by 3.
 Prints 'Buzz' if the number is only divisible by 5.
 Prints the number if the number is neither divisible by 3 nor 5 """

def fizzBuzz(upTo):
    for i in range(1, upTo + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")

# Exercise 6 --> Ordinal Suffix
"""Write an ordinalSuffix() function with an integer parameter named number and returns a string of the
number with its ordinal suffix. For example, ordinalSuffix(42) should return the string'42nd' """

def ordinalSuffix(number):
    if number % 10 == 1 and number % 100 != 11:
        return f"{number}st"
    elif number % 10 == 2 and number % 100 != 12:
        return f"{number}nd"
    elif number % 10 == 3 and number % 100 != 13:
        return f"{number}rd"
    else:
        return f"{number}th"
    
assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == '1st'
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'

# Exercise 7 --> Ascii Table
""" Write a printASCIITable() function that displays the ASCII number and its corresponding text character, from 32 to 126.
(These are called the printable ASCII characters.) use the ord() and chr() functions to translate between integers and text characters. """

def printASCIITable():
    for i in range(32, 127):
        print(f"{i}--> {chr(i)}")
printASCIITable()

# Exercise 8 --> Read And Write File
""" Write a writeToFile() function with two parameters for the filename of the file and the text to write into the file.
Second, write an appendToFile() function, which is identical to writeToFile() except that the file opens in append mode instead of write mode. 
Finally, write a readFromFile() function with one parameter for the filename to open. This function returns the full text contents of the file as a string """

def writeToFile(filename, text):
    with open(filename, "w") as file:
        file.write(text)
        
def appendToFile(filename, text):
    with open(filename, "a") as file:
        file.write(text)
        
def readFromFile(filename):
    with open(filename, "r") as file:
        return file.read()