
def fruit_distribution(s,n):
    """
    Is task mein, aapko ek string di jayegi jo ek fruit basket mein distribute kiye gaye apples aur oranges ki sankhya ko darshati hai. Ye basket mein apples, oranges, aur mango fruits hote hain. Diye gaye string se jo total number of oranges aur apples ko darshati hai aur ek integer jo basket mein total fruits ki sankhya ko darshati hai, use use karke basket mein mango fruits ki sankhya return karo.
    Jaise ki:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    if n==0:
        return 0
    else:
        if s[0] == "0" or s[0] == "0000" or s[0] == "000":
            return s[1:]-n
        elif s[0] == "1":
            return n-1
        elif n == len(s):
            for i in s:
                if i!= "0":
                    return i
            return -n

if __name__ == '__main__':
    test = "5 apples and 6 oranges"
    print test in fruits_baskets(test)
    test = "6 apples, 1 orange and 5 oranges"
    print test in fruits_baskets(test)
    test = "10 apples and 6 oranges"
    print test in fruits_baskets(test)
    test = "1 orange and 5 oranges"
    print test in fruits_baskets(test)
    test = "6 apples and 7 oranges"
    print test, test not in fruits_baskets(test)
    test = "1 appels and 5 oranges"
    print test not in fruits_baskets(test)
    test = "100 apples and 1 oranges