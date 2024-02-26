
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
    # write your code
    if need > remaining:
        need = remain
    elif need < remaining:
        need = 0

    return list(np.linspace(0, remaining, need + 1)) + [(remaining,) + ([0] * (need - 1))]


if __name__ == '__main__':
    num_tests = int(input())
    for _ in range(num_tests):
        # read test case
        t, _ = map(int, input().split())

        requests = map(int, raw_input().strip().split(' '))
        total = sum(requests)
        # remove first
        requests.pop(0)

        remaining = 0
        for value in requests:
            try:
                remaining += value
            except OverflowError:
                remaining += int(1e+9)
                print()
                continue

        solutions = eat(total, t, remaining)
        for answer in solutions:
            print(sum(