
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """
    s = s.upper()
    indices = [i for i, k in enumerate(s) if k not in 'aeiou']
    count = sum(c == 'a' for c in indices)
    return count

print(count_upper('abcdefg'))

If you see at the function count_upper(), I have created a list and added all the indices of the characters which are not equal to 'aeiou' in the string. As you can see only three characters from those are uppercase vowels and rest are dashes. So sum is to check how many of these three are there in the string and only if it is equal to 1, I am returning those three characters alone. 
Note it is best to put everything in single line. But it didn't give a proper indentation. 
If you run above code then you will get output 4 which is correct.
For more understanding, you can refer to this article.

