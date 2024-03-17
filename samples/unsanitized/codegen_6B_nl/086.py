
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

    # Convert string to list, woh string hoti hai
    list = s.split(' ')
    # Use reverse to convert karna list karna list ke bhi bhala

    # Use anti-counter to get count of words
    words = len(list) - list.count(' ')

    # Use anti-counter to get count of characters
    length = len(list[0]) - list[0].count(' ')

    # Iterate through words
    for word in list:
        # Convert word to ascii value
        word = ord(word)
        # Change order to ascending: (97..122) in ascii
        word = word - list.count(' ') + 97
        # Add word to a list of characters
        list[-1] = list[-1] + str(word) +''
        # Use anti-counter to get count of characters
        index = list[-1].find(' ')
        if index > 0: