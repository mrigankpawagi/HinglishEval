def hex_key(num):
    prime_hex = ["2", "3", "5", "7", "B", "D"]
    return sum(1 for digit in num if digit in prime_hex)
