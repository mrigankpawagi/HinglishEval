
def rounded_avg(n, m):
    """You are given two positive integers n and m, and your task is to compute the
    average of the integers from n through m (including n and m). 
    Round the answer to the nearest integer and convert that to binary.
    If n is greater than m, return -1.
    Example:
    rounded_avg(1, 5) => "0b11"
    rounded_avg(7, 5) => -1
    rounded_avg(10, 20) => "0b1111"
    rounded_avg(20, 33) => "0b11010"
    """
    if n>m:
        return -1
    rounddic = { }
    for i in range(n,m+1):
        a = bin(i)[2:]
        if a not in rounddic:
            rounddic[a]=i
        else:
            rounddic[a]+=i
    return sum(rounddic.values())













#test = [5,10,11,15,20]

"""
#print rounded_avg(5, 10), "->", rounded_avg(11, 15), "->", rounded_avg(15, 20)

print rounded_avg(15, 20), rounded_avg(20, 30), rounded_avg(30, 40)

#test = [5,10]
#print rounded_avg(5, 10), "->", rounded_avg(10, 15), "->", rounded_avg(15, 20)

#test = [11,15,20]
#print rounded_avg(11, 15), "->", rounded_avg(15, 20)


print rounded_avg(15, 20), rounded_avg(20, 30), rounded_avg(30, 40)

print rounded_avg("111110")
print rounded_avg("11010011010")
print rounded_avg("01101000")
print rounded_avg("01101000")
print rounded_avg("1111100110")
#print rounded_avg(100, 200)

#input a