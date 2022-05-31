
def fibonacci(n):
    assert n >= 0 and int(n) == n, "The number must be a positive integer only!"

    if n in [0, 1]:
        return n

    return fibonacci(n-1) + fibonacci(n-2) 
    # Without memoization there are many repeated calls with the same n

print(fibonacci(8))