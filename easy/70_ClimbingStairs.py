def climbStairs(n):
    # Fibonacci/DP/Memoization
    # Add 1 step to all the steps 1 below target
    # Add 2 step to all the steps 2 below target
    # Hence solution is sum of ways(target-1)+ways(target-2)
    a = b = 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(climbStairs(5))