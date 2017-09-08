
def factorialize(n):
    total = 1
    for a in range(1, n + 1):
        total = total * a
    return total

print(factorialize(5))
