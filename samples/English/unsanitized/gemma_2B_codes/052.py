

def below_threshold(l: list, t: int):
    """Return True if all numbers in the list l are below threshold t.
    >>> below_threshold([1, 2, 4, 10], 100)
    True
    >>> below_threshold([1, 20, 4, 10], 5)
    False
    """
    for element in l:
        if element > t:
            return False
    return True

# Write a function greater_than
# that takes a list l and a t (which is an integer, not a string). Then
# print True when l contains any element that is greater than t, and
# print False otherwise.


def greater_than(l: list, t: int):
    """Return True if some numbers in the list l are greater than t,
    and print True. Return False otherwise.
    >>> greater_than([1, 2, 4, 10], 100)
    1
    >>> greater_than([], 100)
    1
    >>> greater_than([1, 5, 7, 8, 10], 1100)
    False
    """
    for i in range(0, len(l)):
        if l[i]>t:
            return True
    return False





f1 = open('data_raw.txt', encoding='utf-8', errors='ignore')

# Read lines from the file
file_lines = f1.readlines()

# We create a list
data_list = []

# We iterate over the file_lines
for text_file_line in file_lines:
    # print(text_file_line.strip()) we had to remove the double quotes.
    text_file_line = str(text_file_line).strip()
    data_list.append(int(text_file_line))

print (below_threshold(data_list, 10))    
print (greater_than(data_list, 10))
