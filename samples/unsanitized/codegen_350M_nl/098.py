
def count_upper(s):
    """
    Diye gaye string s mein, even indices par kitne uppercase vowels hai, unhe count karo.

Jaise ki:
count_upper('aBCdEf') returns 1
count_upper('abcdefg') returns 0
count_upper('dBBE') returns 0
    """
    for d in s:
        for i in range(len(d)):
            if 'a' in d: {
                count_upper(d.encode('utf-8').unpack('b*b'))
            }

for n, z in map(str, count_upper):
        n_str = n.upper()
        print n_str

count the rows and count the spaces (printing 2) or 4 the spaces, and print it in the form:
aBCdEf

Thanks to all my friends for sending me links to the other pages, and
for comments that I made.

A:

There are a few problems in your for loop.
First, count_upper only works backwards and counting the spaces is invalid. You cannot start counting with an empty string because then you have to write "abcdefg" to count the extra spaces. You can work into a list (which will be a copy of s) instead and then count the spaces with something like this:
for z, w in zip(s, count_uppercase(s[-1])):
    print "%s" % (z, w)

It doesn't look like you actually use the number 4.

