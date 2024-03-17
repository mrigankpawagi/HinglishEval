
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
    return _make_sentence(s).replace('\xa0','')

import ui4


_make_sentence = lambda s: (u"- " if s!= '' else u"- ").join(u''+ s).strip()
