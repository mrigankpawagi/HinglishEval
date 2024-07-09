
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) <= 1:
        return False
    prime = 2
    for i in string:
        if i % prime == 0:
            return False

    return True

A:

Just a short recap for you (and for future readers): strings consist of characters. Characters are a certain amount of bytes. Therefore: Every string is made of one or more bytes (one character), not more, nor less.
You are correct that any given UTF-8 character code points from 0 - 0x7F, so you can certainly just ignore the 0 byte and treat your strings as bytes.
But you are wrong in stating that a string is "made of one or more bytes". This is not true (unless your implementation is the infamous "endianness" byte order). For example any string literal is just one byte: 'Hello\x00there\x00'
You can use chr(0) to convert a value to a character. Here:
my_string = 'F'*100   # a big string of ones
print('My string has {0} chars: {1}, is {2} bytes long'.format(len(my_string),my_string,len(my_string)))
# My string has 0 chars: F, is 111 bytes long

Another thing to clear (and why this answer exists...)
When you're converting bytes (i.e. single characters) to another character (i.e. strings), you have to take into account the endianness of the system. This ends up being an irrelevant detail when it comes to strings and Unicode. The endianness of a system is just one byte.
So using your question title:

The question as written is about converting between a unicode string and a byte