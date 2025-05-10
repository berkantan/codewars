# QUESTION-3
# Write a function that takes an integer as input, and returns the number of bits that are equal to one 
# in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    binary = ""
    count = 0
    while n > 0:
        if n % 2 == 1:
            binary += "1"
            n = n // 2
        elif n % 2 == 0:
            binary += "0"
            n = n // 2
        if n == 0:
            binary += "0"
    binary = binary[:: -1]
    for i in binary:
        if i == "1":
            count +=1
    return count
    

