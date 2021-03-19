def fibonacci(limit):
    lookup = [0, 1]
    for i in range(limit-2):
        lookup.append(lookup[-2]+lookup[-1])
    return lookup[:limit]

print(fibonacci(6))