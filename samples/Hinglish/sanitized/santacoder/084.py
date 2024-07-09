
def solve(N):
    """
    Diye gaye positive integer N ka, uske digits ka total sum binary mein return karo.
    
    Udaharan
        Agar N = 1000 hai, to digits ka sum hoga 1 aur output honi chahiye "1".
        Agar N = 150 hai, to digits ka sum hoga 6 aur output honi chahiye "110".
        Agar N = 147 hai, to digits ka sum hoga 12 aur output honi chahiye "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         binary number ka ek string
    """
    sum = 0
    temp_num = 0
    temp_digit = ""
    number_str = '0'
    for _ in range(N):
        # To sum and keep track of all the digits in a given number. 
        sum += digit_adder(temp_digit, N + sum)
        temp_num += 1
        temp_digit = ''
        # Update the number string based on the temp_number from which we have just summed.
        # Add first digit from temp_num and then update temp_digit.
        for _ in range(len(str(temp_num))):
            temp_digit += str(temp_num)[:len(str(temp_num)) - 1]
        # Update temp_num to 0.
    # To add remaining digits. To sum them in reverse order and keep track of the ones and zeros in an array.
    # Add remaining digits only if there are zeroes in the last digit of the sum.
    ones = sum - temp_num
    zeros = N - ones
    if zeros == 0:
        ones -= 10
    if zeros > 10:
        zeros -= 100
        ones -= 1000
    temp_arr = zeros
    print(ones)
    while ones > 0:
        temp_arr += ones
        ones = 0
        if temp_arr > 1: 
            temp_arr -= 1000
        if temp_arr > 100:
            temp_arr -= 100
            ones -= 100
        if temp_