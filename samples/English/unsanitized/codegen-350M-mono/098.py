
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    s = s.upper()    # convert to uppercase
    if s.isdigit(): # filter out numbers
        return int(s)
    vowels = ['A', 'E', 'I', 'O', 'U']    # list of vowels
    upper_ind = lambda i: sum(c.isdigit() for c in s[i]) in {2, 4, 6} # function to check
    return sum(1 for i in range(0,len(s)) if upper_ind(i)) - sum(1 for i in range(0, len(s)) if not upper_ind(i)) 

# (1) Test Cases
test_cases = [
    (string2('aBCdEf'), 1),
    (string2('abcdefg'), 4)
]
for s,n in test_cases:
   print(count_upper(s))