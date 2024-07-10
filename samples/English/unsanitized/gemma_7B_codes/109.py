
def move_one_ball(arr):
    """
    Humare paas ek array 'arr' hai N integers arr[1], arr[2], ..., arr[N] ka. Array mein numbers randomly order mein honge. Aapka task hai yeh determine karna ki kya hume non-decreasing order mein sorted array mil sakta hai, diye gaye array par niche diye gaye operation ko perform karke:
        Aapko right shift operation ko kitni bhi baar perform karne ki anumati hai.
    
    Ek right shift operation ka matlab hai array ke saare elements ko ek position right direction mein shift karna. Array ka last element array ke starting position yaani 0th index par move ho jayega. 

    Agar upar diye gaye operation ko perform karke sorted array mil sakta hai to True return karo, nahi to False return karo.
    Agar diya gaya array khali hai to True return karo.

    Note: Diye gaye list mein unique elements honge.

    Udaharan ke liye:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: 2 right shift operations perform karke, diye gaye array ke liye non-decreasing order prapt kiya ja sakta hai.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation: Kisi bhi number of right shift operations perform karke diye gaye array ke liye non-decreasing order prapt karna sambhav nahi hai.
    """
    
    # Complete this function
    N = len(arr)
    right_shift_max = N-arr[-1]+1
    left_shift_max = arr[0]-1
    if (right_shift_max + left_shift_max) > N or (1 + N-arr[0]) > N or (1 > N-arr[-1]):
        return False
    else: 
        return True
    
    
    
    
def main():
    print(move_one_ball([3, 4, 5, 1, 2]))
    print(move_one_ball([3, 5, 4, 1, 2]))
    
if __name__ == '__main__':
    main()
