import sys

min, max = int(sys.argv[1]), int(sys.argv[2])

def multiples_addition(min_range, max_range):
    total = 0
    for i in range(min_range, max_range):
        if i % 3 == 0 or i % 5 == 0:
            total += i

    return total

print(multiples_addition(min, max))
