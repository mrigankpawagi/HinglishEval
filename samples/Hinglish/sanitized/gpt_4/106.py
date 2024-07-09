def f(n):
    def factorial(i):
        if i == 0 or i == 1:
            return 1
        else:
            return i * factorial(i - 1)

    def sum_numbers(i):
        return sum(range(1, i + 1))

    return [factorial(i) if i % 2 == 0 else sum_numbers(i) for i in range(1, n + 1)]
