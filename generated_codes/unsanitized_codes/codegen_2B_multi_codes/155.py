def even_odd_count(num):
    """
    Ek integer diya gaya hai. Ek tuple return karo jo even aur odd digits ki sankhya ko kramashah darshata hai.

     Udaharan:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    even_odd_count = [(num % 2) * 2, (num % 2)]
    while num > 0:
        even_odd_count[0] += 1
        even_odd_count[1] += 2
        num /= 2
    return even_odd_count[::-1]


# Testing the solution
test_list = [(-10), (0), (10), (100)]
print("First example", even_odd_count(test_list[0]))
print("Second example", even_odd_count(test_list[1]))
print("Third example", even_odd_count(test_list[2]))
print("Fourth example", even_odd_count(test_list[3]))

# Test the solution against an online test case
test_cases = [(123, (1, 2)), (234, (-13, 5)), (-4, (0, 1))]
for test in test_cases:
    a, b = test
    res_even_odd = even_odd_count(a)
    res_delta = list(map(lambda x: x - a, res_even_odd))
    if res_delta == b:
        print("Solution is correct for", a, "and", b)
    else:
        print(a, "->", res_even_odd)
