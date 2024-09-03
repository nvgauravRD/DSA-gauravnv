import math

# function returns sum of digits of a number 
def CountDigits(n) -> int:
    return math.floor(math.log10(n) + 1)

# printing the output
print(CountDigits(123)) # O/p: 3