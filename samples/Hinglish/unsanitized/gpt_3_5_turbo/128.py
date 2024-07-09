def prod_signs(arr):
    if len(arr) == 0:
        return None
    
    magnitude_sum = 0
    sign_product = 1
    
    for num in arr:
        magnitude_sum += abs(num)
        sign_product *= num
    
    return magnitude_sum * sign_product