
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels=['a','e','i','o','u']
    counter = 0
    
    for i in range(len(s)):  
        if s[i].lower() in vowels and (i%2 == 0):
            counter += 1
    return counter
  
  

# Driver code
if __name__ == "__main__":
    s = 'aBCdEf'
    print("Expected: 1, Actual:", count_upper(s))
    s = 'abcdefg'
    print("Expected: 0, Actual:", count_upper(s))
    s = 'dBBE'
    print("Expected: 0, Actual:", count_upper(s))
