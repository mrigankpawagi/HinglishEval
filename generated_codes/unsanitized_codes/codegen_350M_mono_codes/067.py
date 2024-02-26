
def fruit_distribution(s,n):
    """
    Is task mein, aapko ek string di jayegi jo ek fruit basket mein distribute kiye gaye apples aur oranges ki sankhya ko darshati hai. Ye basket mein apples, oranges, aur mango fruits hote hain. Diye gaye string se jo total number of oranges aur apples ko darshati hai aur ek integer jo basket mein total fruits ki sankhya ko darshati hai, use use karke basket mein mango fruits ki sankhya return karo.
    Jaise ki:
    fruit_distribution("5 apples and 6 oranges", 19) ->19 - 5 - 6 = 8
    fruit_distribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
    fruit_distribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
    fruit_distribution("100 apples and 1 oranges",120) -> 120 - 100 - 1 = 19
    """
    count = 0

    if s.isdigit():
        for k in range(1, int(n)+1):
            count += int(s)//k
            res = count % 10

            if res!= 0:
                if res < 10:
                    return int(res)
                else:
                    return res
            else:
                result = int(s[:: -1])

                if result > 0:
                    if result%10 == 0:
                        count += result//10 - 1

                    else:
                        count += result//10
                else:
                    return result%10

    else:
        for k in range(n+1):
            count += int(s[::-1])//int(k)

            if count > 0:
                break
            else:
                return int(s[::-1])//int(k)
    

    return count

print(fruit_distribution("5 oranges and 6 apples", "21"))