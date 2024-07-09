def exchange(lst1, lst2):
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    even_lst2 = [num for num in lst2 if num % 2 == 0]
    if len(odd_lst1) <= len(even_lst2):
        return "YES"
    else:
        return "NO"