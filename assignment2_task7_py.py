
import time

# Original recursive method
def ways_naive(n):
    if n <= 1:
        return 1

    return ways_naive(n - 1) + ways_naive(n - 2)


# Redesigned iterative method
def ways_loop(n):
    if n <= 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    return b


for n in [10, 20, 25, 30]:
    start = time.perf_counter()
    original = ways_naive(n)
    original_time = time.perf_counter() - start

    start = time.perf_counter()
    redesigned = ways_loop(n)
    redesigned_time = time.perf_counter() - start

    print("\nn =", n)
    print("Original result:", original)
    print("Redesigned result:", redesigned)
    print("Original time:", round(original_time, 6))
    print("Redesigned time:", round(redesigned_time, 6))
    print("Same result:", original == redesigned)
