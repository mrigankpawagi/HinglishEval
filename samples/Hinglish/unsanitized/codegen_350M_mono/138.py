
def is_equal_to_sum_even(n):
    """
    Evaluate karo ki diya gaya number n kya exactly 4 positive even numbers ka sum ho sakta hai
    Udaharan
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n<=4 and n%2==0:
        return False
    if n==4 or n==6 or n==8:
        return True
    for i in range(1,5):
        if n%i==0:
            if is_equal_to_sum_even(n//i)==False:
                return False
    return True


num = is_equal_to_sum_even(4)
print(num)
print("------------------")

# 3 kuch hai
# num2 = 4
# kar = is_equal_to_sum_even(num2)
# if kar==False:
#     print("daha kiya hai")
# else:
#     print("daha kugih")



# 4 karo hai
# count = 0
# for i in range(1,6):
#     num = int(input("enter number " + str(i)))
#     if num%2==0:
#         count+=1
# print("all even numbers aplhabet = " + str(count))




for i in range(1,6):
    num = int(input("enter number " + str(i)))
    sum=0
    for _ in range(0,num):
        sum+=int(input("enter number of next digit "))
    if sum==(10**i):
        print(num," is positive number")
        break
else:
    print(num," is not positive number")


