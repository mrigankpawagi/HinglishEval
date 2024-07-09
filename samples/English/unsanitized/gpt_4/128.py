def prod_signs(arr):
    if not arr:
        return None
    else:
        sign_product = 1
        magnitude_sum = 0
        for num in arr:
            if num < 0:
                sign_product *= -1
                magnitude_sum += abs(num)
            elif num > 0:
                sign_product *= 1
                magnitude_sum += abs(num)
        return sign_product * magnitude_sum