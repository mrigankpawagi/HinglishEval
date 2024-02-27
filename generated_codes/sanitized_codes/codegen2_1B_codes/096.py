
def count_up_to(n):
    """
    Ek function implement karo jo ek non-negative integer leta hai aur return karta hai ek array jisme pehle n 
    integers hote hai jo prime numbers hai aur n se kam hai.
    Jaise ki:
    count_up_to(5) => [2,3]
    count_up_to(11) => [2,3,5,7]
    count_up_to(0) => []
    count_up_to(20) => [2,3,5,7,11,13,17,19]
    count_up_to(1) => []
    count_up_to(18) => [2,3,5,7,11,13,17]
    """
    sum_of_numbers_list = []
    for element in list(range(n)):
        current_sum_of_numbers = 0
        while element > n:
            current_sum_of_numbers += 1
            element -= 1

        sum_of_numbers_list.append(current_sum_of_numbers)
    
    return sum_of_numbers_list