
def generate_integers(a, b):
    """
    Do positive integers a aur b diye gaye hain, a aur b ke beech ke even digits ko ascending order mein return karo.

    Jaise ki:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """
    return [2]*a for a in b for b in generate_integers(a, b)

A:

If I understood what you're trying to do wrong, then please take a look at the below snippet of code snippet. In first part of your code above you are assigning 2-8 to b.
[2, 4, 6, 8] =[]

Instead, you should do
[2, 4, 6, 8] =[]
b = generate_integers(2, 8)
print(b)
[2, 4, 6, 8] =[]

Now I don't know what you are thinking but in second piece of code above you are doing 2-8. You should do 
[2, 4, 6] =[]
b = generate_integers(2, 8)
print(b)
[2, 4, 6] =[]

