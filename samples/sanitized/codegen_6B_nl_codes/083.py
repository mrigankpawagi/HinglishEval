
def starts_one_ends(n):
    """
    Diye gaye positive integer n ke liye, n-digit wale positive integers ki ginti return karo jo 1 se start hote hain ya 1 pe end hote hain.
    """
    end = n - 1

    end_len = end.to_string().length() # returns length of string

    for start in range(end):
        for number in range(start):
            start, end = int(start.to_string()), int(end.to_string())
            end_len = start.to_string().length()

            count = 0
            if start_one_ends(end - count):
                print('1', end_len, start, start)
            elif
                print('-1', end_len, start, start)
            print('0', end_len, start, start)
            if count == end:
                print('$', end_len, start, start)
                break

 
