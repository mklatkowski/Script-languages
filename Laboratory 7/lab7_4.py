from functools import lru_cache

def make_generator(f):
    @lru_cache()
    def memoized_f(n):
        return f(n)

    def generator():
        n = 1
        while True:
            yield f(n)
            n += 1
    return generator()

def fibonacci(n):
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

fibonacci_generator = make_generator(fibonacci)
print(next(fibonacci_generator))
print(next(fibonacci_generator))
print(next(fibonacci_generator))
print(next(fibonacci_generator))
print(next(fibonacci_generator))

geometry_generator = make_generator(lambda x: 2**x)
print(next(geometry_generator))
print(next(geometry_generator))
print(next(geometry_generator))
print(next(geometry_generator))
print(next(geometry_generator))
