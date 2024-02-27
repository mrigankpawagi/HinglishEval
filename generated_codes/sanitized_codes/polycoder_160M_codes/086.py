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
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """  # if s is non-empty, it's an empty list so there's no need to shuffle
    if len(s) == 0:
        return s
    # for word, return it as a string
    for word in s:
        # if word is not an empty string, return it as it is
        if word in anti_shuffle(word):
            return word
    # no word found.   do something here
    else:
        return s
