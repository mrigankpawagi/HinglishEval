def fruit_distribution(s, n):
    """
    Is task mein, aapko ek string di jayegi jo ek fruit basket mein distribute kiye gaye apples aur oranges ki sankhya ko darshati hai. Ye basket mein apples, oranges, aur mango fruits hote hain. Diye gaye string se jo total number of oranges aur apples ko darshati hai aur ek integer jo basket mein total fruits ki sankhya ko darshati hai, use use karke basket mein mango fruits ki sankhya return karo.
    Jaise ki:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    s = str(s)
    n = int(n)
    if n <= 0:
        return 0
    max = str(s).find(" ") + 1
    string = ""
    while s[0] != "":
        if s[0:1] == ",":
            c = s[1]
            string = ", ".join(s.split(c))
        else:
            break
    for i in range(1, max):
        s = s1.split(" ")
        if len(s) > 1:
            s.pop(0)
    if len(s) == 1:  # single fruit not found
        return 0
    num = len(s) - 1