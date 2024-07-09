def fruit_distribution(s, n):
    """
    Is task mein, aapko ek string di jayegi jo ek fruit basket mein distribute kiye gaye apples aur oranges ki sankhya ko darshati hai. Ye basket mein apples, oranges, aur mango fruits hote hain. Diye gaye string se jo total number of oranges aur apples ko darshati hai aur ek integer jo basket mein total fruits ki sankhya ko darshati hai, use use karke basket mein mango fruits ki sankhya return karo.
    Jaise ki:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    # Write your code here
    s = s.split(" ")
    apples = int(s[0].split(" ")[1])
    oranges = int(s[2].split(" ")[1])
    total_fruits = int(s[4])
    return total_fruits - apples - oranges
