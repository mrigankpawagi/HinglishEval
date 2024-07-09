
def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots,
    but now you need to eat more carrots to complete the day's meals.
    you should return an array of [ total number of eaten carrots after your meals,
                                    the number of carrots left after your meals ]
    if there are not enough remaining carrots, you will eat all remaining carrots, but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer
        the number of carrots that you have eaten.
    @need : integer
        the number of carrots that you need to eat.
    @remaining : integer
        the number of remaining carrots thet exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000

    Have fun :)
    """
    need = int(need)
    remaining = int(remaining)
    # if all the above conditions were met, return an array of length of needed number of carrots
    if remaining >= need: return [ need, remaining ]

    # if need is 0 the array length is defined by 0, so we have to reset it to all zeros
    else:
        length1 = next(i for i in range(0, need))
        length2 = len(list(reversed(list(list(map(add, list(range(0, length1))))))) - number)
        length3 = next(i for i in range(0, length2))
        total = 0
        return [need, remaining]


## Your code here
