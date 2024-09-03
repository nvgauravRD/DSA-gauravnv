# the below function returns sum of digits of a number
def SumOfDigits(n) -> int:
    sum_of_digits = 0

    while n!=0:
        sum_of_digits += (n%10)
        # remove floating values after division
        n = int(n/10)

    return sum_of_digits

print(SumOfDigits(1234)) # O/P : 10