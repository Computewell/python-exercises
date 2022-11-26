""" 
You will write four functions for this exercise. 
The functions area() and perimeter() have length and width parameters
and the functions volume() and surfaceArea() have length,width, and height parameters.
These functions return the area, perimeter, volume, and surface area, respectively 
"""

def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)

def volume(length, width, height):
    return length * width * height

def surfaceArea(length, width, height):
    return 2 * (length * width + length * height + width * height)
#Test Cases
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