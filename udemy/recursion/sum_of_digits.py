
def sum_of_digits(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"

    if n == 0:
        return 0
    
    quotient = n//10
    remainder = n%10

    return remainder + sum_of_digits(quotient)

print(sum_of_digits(2222))