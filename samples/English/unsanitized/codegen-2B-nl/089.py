
def encrypt(s):
    """Create a function encrypt that takes a string as an argument and
    returns a string encrypted with the alphabet being rotated. 
    The alphabet should be rotated in a manner such that the letters 
    shift down by two multiplied to two places.
    For example:
    encrypt('hi') returns 'lm'
    encrypt('asdfghjkl') returns 'ewhjklnop'
    encrypt('gf') returns 'kj'
    encrypt('et') returns 'ix'
    """
    new_letters = list(s)
    new_letters[0] = 'a'
    for x in range(1, len(s)):
        x = '_' + new_letters[x]
        new_letters[x] = 'a'
    return ''.join(new_letters)

if __name__ == '__main__':
 s = 'z'
 print (functools.reduce(lambda a, b: a + b,functools.reduce(lambda a, b: a + b, set(list(_) + set([_]))), ''))

A:

It is very possible to learn to read this code.

It is a small program, but it doesn't do anything. It just makes a function out of random. And so far I see no purpose for you actually using the functions you make out of random.

it requires a new function to operate over list of words. The function can be very simple. But if you would like to add more and more fancy features. You would have to repeat it again and again for every new feature you add. This would require to repeat the code over and over again.

Python tries to help you to understand the language. You can look for examples in the python docs online.

if __name__ == "__main":
    print("Hello, World!", file=sys.stderr)

You never use this sys.stderr = <file name> and you throw it away. So you are actually wasting some cpu-time and memory.

You are returning