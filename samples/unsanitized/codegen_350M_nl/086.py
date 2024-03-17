
def anti_shuffle(s):
    """
    Ek function likho jo ek string leta hai aur uska ordered version return karta hai.
    Ordered version of string, woh string hoti hai jahan saare words (space se separated)
    ko ek naye word se replace kiya jata hai jahan saare characters ko 
    unke ascii value ke basis pe ascending order mein arrange kiya jata hai.
    Dhyan do: Aapko words aur blank spaces ki order sentence mein maintain karni chahiye.

    Jaise ki:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """
    def get(pos,s):
        return s.join('',left=1)
    for i,word in six.iteritems(s): # iterated word
        try:
            word = word.lower()
        except NameError:
            word = word.upper()
        assert(word in get(pos,s))
    return (get(pos,s.replace(' ', '')),
            get(pos,s))

The original post shows a more complicated function. It is not clear why it is used to replace word.replace, and how that can be used.
Update
I found this interesting post.
I was unable to solve all the issues with that code, so I made the code as below:
