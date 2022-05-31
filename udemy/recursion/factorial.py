import sys
sys.setrecursionlimit(2000)

def factorial(n):
    # Input validation
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"

    # Base case
    if n in [0, 1]:
        return 1
    
    # Recursive case
    return n * factorial(n-1)

print(factorial(5))