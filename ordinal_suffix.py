"""
Write an ordinalSuffix() function with an integer parameter named number 
and returns a string of the number with its ordinal suffix.
For example, ordinalSuffix(42) should return the string'42nd'
"""

def ordinalSuffix(number):
    if number % 10 == 1 and number % 100 != 11:
        return f"{number}st"
    elif number % 10 == 2 and number % 100 != 12:
        return f"{number}nd"
    elif number % 10 == 3 and number % 100 != 13:
        return f"{number}rd"
    else:
        return f"{number}th"
# Test Cases
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