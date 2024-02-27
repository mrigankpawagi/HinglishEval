
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
    number_of_balls = len(arr)
    flag = False

    if number_of_balls < 2:
        flag = True

    is_sorted = is_array_in_descending_order(arr)
    if is_sorted:
        flag = True

    arr_copy = arr
    if number_of_balls > 1:
        for i in range(number_of_balls // 2):
            arr_copy.append(arr.pop(