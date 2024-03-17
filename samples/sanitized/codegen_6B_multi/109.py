
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
    #1. To find the index of first max value
    index = 0
    if(0 in arr): index = arr.index(0)
    #2. loop and perform right shift 
    for i in range(1, len(arr) - index):
        arr[index+i-1], arr[i] = arr[i],  arr[index+i-1]

    print ("Move complete " + str(arr))
    return True if arr.sort() else