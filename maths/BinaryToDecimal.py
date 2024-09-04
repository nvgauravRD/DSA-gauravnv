# below function accepts a number and returns binary value for that number
def BinaryToDecimal(num) -> str:
    # storing individual bits
    binary_stack = ""

    # traversing from end
    while num != 0:
        binary_stack += str(num&1) # check last bit 1 or 0 using & 

        # shifting bits to left
        num = num >> 1
    return binary_stack

# since traversal happens from end the result will also be reversed
# finally we reverse to obtain actual value
print(BinaryToDecimal(4)[::-1]) 


